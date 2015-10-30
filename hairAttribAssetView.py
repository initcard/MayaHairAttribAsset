import sys
import json

import maya.cmds as cmds
import pymel.core as pmcore

from PySide  import QtGui, QtCore

import maya_utils.maya_utils as maya_utils

MayaMainWindow = maya_utils.shibokenGetMayaMainWindow()

hairAttribNameList = ["hairsPerClump", "hairColor", "opacity", "specularColor", "specularPower", \
                      "translucence", "diffuseRand"]

class HairAttribCache(QtGui.QDialog):
    def __init__(self, parent=None):
        super(HairAttribCache, self).__init__(parent)
        
        # for models
        self.hairNodesList =[]
        self.cacheAssetList =[]
        
        self.cacheDict = {}
        self.createUi()

    def createUi(self):
        # TODO Create a simple dialog
        # Top layout
        fileNameLabel = QtGui.QLabel("Cache File:")
        self.fileNameLineEdit = QtGui.QLineEdit()
        self.seletCacheFileBtn = QtGui.QPushButton("...")

        topLayout = QtGui.QHBoxLayout()
        topLayout.addWidget(fileNameLabel)
        topLayout.addWidget(self.fileNameLineEdit)
        topLayout.addWidget(self.seletCacheFileBtn)

        # cached attrib list
        self.cachedAttribList = QtGui.QListView()
        self.cachedAttribListModel = QtGui.QStringListModel()
        
        # operation buttons
        self.applyAttribBtn = QtGui.QPushButton("Apply")
        self.saveAttribBtn = QtGui.QPushButton("Cache")
        self.refreshListBtn = QtGui.QPushButton("Refresh")
        buttonsLayout = QtGui.QVBoxLayout()
        buttonsLayout.addWidget(self.applyAttribBtn)
        buttonsLayout.addWidget(self.saveAttribBtn)
        buttonsLayout.addWidget(self.refreshListBtn)

        # hair nodes list
        self.hairNodesListView = QtGui.QListView()
        self.hairNodesListModel = QtGui.QStringListModel()
        
        # bottom layout
        bottomLayout = QtGui.QHBoxLayout()
        bottomLayout.addWidget(self.cachedAttribList)
        bottomLayout.addLayout(buttonsLayout)
        bottomLayout.addWidget(self.hairNodesListView)

        # main layout, vertical
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottomLayout)

        self.setLayout(mainLayout)
        self.setWindowTitle("Hair Attrib Asset")

        # setup connections
        self.seletCacheFileBtn.clicked.connect(self.specifyCacheFile)
        pass

    def readCache(self, fileName):
        # TODO read cache contents from specified file
        with open(fileName, mode='r') as cacheFile:
            self.cacheDict = json.load(cacheFile)

        if not self.cacheDict:
            pmcore.displayError("The cache file is empty...")

        pass

    def appendAttribsToCache(self, cacheFile):
        # TODO append hair attribs to cache file
        pass

    def specifyCacheFile(self):
        # TODO specify the cache file
        (cacheFileName, filter) = QtGui.QFileDialog.getOpenFileName(self, "select cache file", ".", "*.json")
        if not cacheFileName:
            return
        print(cacheFileName)
        self.fileNameLineEdit.setText(str(cacheFileName))
        pass

    def getCachedAttrib(self):
        # TODO get select attribute from cache file
        assetNameList = self.cacheDict.keys()
        return assetNameList
        pass

    def writeCacheFile(self):
        # TODO write cache file
        cacheFileName = str(self.fileNameLineEdit.text())
        with open(cacheFileName, 'w') as cacheFile:
            json.dump(self.cacheDict, cacheFile, indent=4)

        pass

    def getAttribsFromSelectedHairNode(self):
        # TODO create a dict from Selected Hair Node
        attibDict = {}
        index = self.hairNodesListView.currentIndex()
        selectedItem = self.hairNodesListModel.data(index, QtCore.Qt.EditRole)
        
        for attrib in hairAttribNameList:
            attribValue = 
        pass

#dlg = HairAttribCache()
#dlg.show()
