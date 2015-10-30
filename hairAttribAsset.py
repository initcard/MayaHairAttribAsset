import sys
import json

import maya.cmds as cmds
import pymel.core as pmcore

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

    def createUi(self):
        # TODO Create a simple dialog
        # Top layout
        fileNameLabel = QtGui.QLabel("Asset File:")
        self.assetFileNameLineEdit = QtGui.QLineEdit()
        self.seletCacheFileBtn = QtGui.QPushButton("...")

        topLayout = QtGui.QHBoxLayout()
        topLayout.addWidget(fileNameLabel)
        topLayout.addWidget(self.assetFileNameLineEdit)
        topLayout.addWidget(self.seletCacheFileBtn)

        # cached attrib list
        self.cachedAttribListView = QtGui.QListView()
        self.cachedAttribListModel = QtGui.QStringListModel()
        
        # operation buttons
        self.applyAttribBtn = QtGui.QPushButton("Apply")
        self.addAttribToLibBtn = QtGui.QPushButton("Add2Asaset")
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
        bottomLayout.addWidget(self.cachedAttribListView)
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
        
        self.addAttribToLibBtn.clicked.connect(self.appendAttribsToCache)
        self.refreshListBtn.clicked.connect(self.refreshList)
        pass
    
    def refreshList(self):
        # TODO: refresh asset listview and node listview

        # asset list
        print("refreshing cache list")
        cacheFileName = str(self.assetFileNameLineEdit.text())
        if cacheFileName:
            self.readCache(cacheFileName)
            assetStrList = self.assetDict.keys()
            self.cachedAttribListModel.setStringList(assetStrList)
            self.cachedAttribListView.setModel(self.cachedAttribListModel)
        
        # hair nodes list
        print("refreshing node list")
        hairNodesStrList = cmds.ls(type = "hairSystem")
        self.hairNodesListModel.setStringList(hairNodesStrList)
        self.hairNodesListView.setModel(self.hairNodesListModel)
        
        pass

    def readCache(self, fileName):
        # TODO read cache contents from specified file
        with open(fileName, mode='r') as cacheFile:
            self.assetDict = json.load(cacheFile)

        if not self.assetDict:
            pmcore.displayError("The cache file is empty...")
        pass

    def appendAttribsToCache(self):
        # TODO append hair attribs to cache file
        (assetName, ok) = QtGui.QInputDialog.getText(self, "input asset Name", "Asset Name:", inputMethodHints = "untiltled")
        if not ok:
            return
        
        if not assetName:
            pmcore.displayWarning("Pleate enter a name")
            return
        
        attribDict = self.getAttribsDictFromSelectedHairNode()
        
        if self.assetDict.has_key(str(assetName)):
            ok = QtGui.QMessageBox(self, "Replace Asset?", "Replace Asset?")
            if ok:
                self.assetDict[assetName] = attribDict
                self.writeCacheFile()
            else:
                return
        else:
            self.assetDict[assetName]=attribDict                  
            print(assetName)
            self.writeCacheFile()
        pass

    def specifyAssetFile(self):
        # TODO specify the cache file
        (cacheFileName, filter) = QtGui.QFileDialog.getOpenFileName(self, "select cache file", ".", "*.json")
        if not cacheFileName:
            return
        print(cacheFileName)
        self.assetFileNameLineEdit.setText(str(cacheFileName))
        pass

    def getAssetList(self):
        # TODO get select attribute from cache file
        assetNameList = self.assetDict.keys()
        return assetNameList
        pass

    def writeCacheFile(self):
        # TODO write cache file
        cacheFileName = str(self.assetFileNameLineEdit.text())
        with open(cacheFileName, 'w') as cacheFile:
            json.dump(self.assetDict, cacheFile, indent=4)
        pass

    def getAttribsDictFromSelectedHairNode(self):
        # TODO create a dict from Selected Hair Node
        attibDict = {}
        index = self.hairNodesListView.currentIndex()
        selectedItem = self.hairNodesListModel.data(index, QtCore.Qt.EditRole)
        
        for attrib in hairAttribNameList:
            attribValue = cmds.getAttr(selectedItem+"."+attrib) 
            attibDict[attrib] =  attribValue
        
        print(dict)
        return attibDict
        pass

#dlg = HairAttribAsset()
#dlg.show()
