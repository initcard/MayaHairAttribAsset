import sys, os
import json

import maya.cmds as cmds
import pymel.core as pmcore
import pymel.mayautils as pymutils

from PySide  import QtGui, QtCore

import maya_utils.maya_utils as maya_utils

MayaMainWindow = maya_utils.shibokenGetMayaMainWindow()

hairAttribNameList = ["hairsPerClump", "hairColor", "opacity", "specularColor", "specularPower", \
                      "translucence", "diffuseRand"]

class HairAttribAsset(QtGui.QDialog):
    def __init__(self, parent=None):
        super(HairAttribAsset, self).__init__(parent)

        self.assetDict = {}
        self.createUi()

        print()

    def createUi(self):
        # TODO:: Create a simple dialog
        # Top layout
        fileNameLabel = QtGui.QLabel("Asset File:")
        self.assetFileNameLineEdit = QtGui.QLineEdit()
        self.assetFileNameLineEdit.setText(pymutils.getMayaLocation() + \
                                           "\\Python\\Lib\site-packages\\MayaHairAttribAsset\\testAsset.json")
        self.seletCacheFileBtn = QtGui.QPushButton("...")

        topLayout = QtGui.QHBoxLayout()
        topLayout.addWidget(fileNameLabel)
        topLayout.addWidget(self.assetFileNameLineEdit)
        topLayout.addWidget(self.seletCacheFileBtn)

        # cached attrib list
        self.assetAttribsListView = QtGui.QListView()
        self.assetAttribsListModel = QtGui.QStringListModel()

        # operation buttons
        self.applyAttribBtn = QtGui.QPushButton("Apply")
        self.addAttribToLibBtn = QtGui.QPushButton("Add2Asset")
        self.refreshListBtn = QtGui.QPushButton("Refresh")
        buttonsLayout = QtGui.QVBoxLayout()
        buttonsLayout.addWidget(self.applyAttribBtn)
        buttonsLayout.addWidget(self.addAttribToLibBtn)
        buttonsLayout.addWidget(self.refreshListBtn)

        # hair nodes list
        self.hairNodesListView = QtGui.QListView()
        self.hairNodesListModel = QtGui.QStringListModel()

        # bottom layout
        bottomLayout = QtGui.QHBoxLayout()
        bottomLayout.addWidget(self.assetAttribsListView)
        bottomLayout.addLayout(buttonsLayout)
        bottomLayout.addWidget(self.hairNodesListView)

        # main layout, vertical
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottomLayout)

        self.setLayout(mainLayout)
        self.setWindowTitle("Hair Attrib Asset")

        # setup connections
        self.seletCacheFileBtn.clicked.connect(self.specifyAssetFile)

        self.applyAttribBtn.clicked.connect(self.applyAssetAttribs)
        self.addAttribToLibBtn.clicked.connect(self.addAttribsToAssetLib)
        self.refreshListBtn.clicked.connect(self.refreshList)
        pass

    def refreshList(self):
        # TODO:: refresh asset listview and node listview

        # asset list
#        print("refreshing cache list")
        cacheFileName = str(self.assetFileNameLineEdit.text())
        if cacheFileName:
            self.readAssets(cacheFileName)
            assetStrList = self.assetDict.keys()
            self.assetAttribsListModel.setStringList(assetStrList)
            self.assetAttribsListView.setModel(self.assetAttribsListModel)

        # hair nodes list
#        print("refreshing node list")
        hairNodesStrList = cmds.ls(type="hairSystem")
        self.hairNodesListModel.setStringList(hairNodesStrList)
        self.hairNodesListView.setModel(self.hairNodesListModel)

        pass

    def readAssets(self, fileName):
        # TODO: read cache contents from specified file
        with open(fileName, mode='r') as cacheFile:
            self.assetDict = json.load(cacheFile)

        if not self.assetDict:
            pmcore.displayError("The cache file is empty...")
        pass

    def addAttribsToAssetLib(self):
        # TODO: append hair attribs to cache file
        (assetName, ok) = QtGui.QInputDialog.getText(self, "input asset Name", "Asset Name:", inputMethodHints="untiltled")
        if not ok:
            return

        if not assetName:
            pmcore.displayWarning("Pleate enter a name")
            return

        attribDict = self.getAttribsDictFromSelectedHairNode()

        if self.assetDict.has_key(assetName):
            ok = QtGui.QMessageBox.question(self, "Replace Asset?", "Replace Asset?", \
                                            QtGui.QMessageBox.Yes, \
                                            QtGui.QMessageBox.No)
            if ok == QtGui.QMessageBox.Yes:
                print(ok, type(ok), QtGui.QMessageBox.Yes)
                self.assetDict[assetName] = attribDict
                self.writeCacheFile()
            else:
                return
        else:
            self.assetDict[assetName] = attribDict
#            print(assetName)
            self.writeCacheFile()

        self.refreshList()
        pass

    def specifyAssetFile(self):
        # TODO: specify the cache file
        (cacheFileName, filter) = QtGui.QFileDialog.getOpenFileName(self, "select cache file", ".", "*.json")
        if not cacheFileName:
            return
#        print(cacheFileName)
        self.assetFileNameLineEdit.setText(str(cacheFileName))
        pass

    def getAssetList(self):
        # TODO: get select attribute from cache file
        assetNameList = self.assetDict.keys()
        return assetNameList
        pass

    def writeCacheFile(self):
        # TODO: write cache file
        cacheFileName = str(self.assetFileNameLineEdit.text())
        with open(cacheFileName, 'w') as cacheFile:
            json.dump(self.assetDict, cacheFile, indent=4)
        pass

    def getAttribsDictFromSelectedHairNode(self):
        # TODO: create a dict from Selected Hair Node
        attibDict = {}
        index = self.hairNodesListView.currentIndex()
        selectedItem = self.hairNodesListModel.data(index, QtCore.Qt.EditRole)
        if not selectedItem:
            pmcore.displayError("You must select a item in the hair node list.")
            return

        for attrib in hairAttribNameList:
            attribValue = cmds.getAttr(selectedItem + "." + attrib)
            attibDict[attrib] = attribValue

#        print(dict)
        return attibDict
        pass

    def applyAssetAttribs(self):
        # TODO: set hair node attribs from asset

        index = self.assetAttribsListView.currentIndex()
        selectedAttribAsset = self.assetAttribsListModel.data(index, QtCore.Qt.EditRole)
        if not selectedAttribAsset:
            pmcore.displayError("You must select a asset item in the asset list.")
            return

        attribs = self.assetDict[selectedAttribAsset]
#        print(attribs)

        index = self.hairNodesListView.currentIndex()
        selectedHairNode = self.hairNodesListModel.data(index, QtCore.Qt.EditRole)
        if not selectedHairNode:
            pmcore.displayError("You must select a node in the hair node list.")
            return

        for attrib in hairAttribNameList:
            nodeAttrib = pmcore.general.PyNode(str(selectedHairNode + '.' + attrib))

            value = attribs[attrib]
#            print(value)
            # value type is int or float
            if type(value) is type(1) or type(value) is type(1.0):
                nodeAttrib.set(value)

            # value type is list
            if type(value) is type([]):
                nodeAttrib.set(value[0])

#        print(selectedHairNode)

