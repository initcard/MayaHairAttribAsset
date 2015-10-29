import sys
import json

import maya.cmds as cmds
# import pymel.core as pmcore

from PySide  import QtGui, QtCore

import maya_utils.maya_utils as maya_utils

MayaMainWindow = maya_utils.shibokenGetMayaMainWindow()

class HairAttribCache(QtGui.QDialog):
    def __init__(self, parent=None):
        super(HairAttribCache, self).__init__(parent)

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
        # operation buttons
        self.applyAttribBtn = QtGui.QPushButton("Apply")
        self.saveAttribBtn = QtGui.QPushButton("Cache")
        self.refreshListBtn = QtGui.QPushButton("Refresh")
        buttonsLayout = QtGui.QVBoxLayout()
        buttonsLayout.addWidget(self.applyAttribBtn)
        buttonsLayout.addWidget(self.saveAttribBtn)
        buttonsLayout.addWidget(self.refreshListBtn)
        # hair nodes list
        self.hairNodesList = QtGui.QListView()
        # bottom layout
        bottomLayout = QtGui.QHBoxLayout()
        bottomLayout.addWidget(self.cachedAttribList)
        bottomLayout.addLayout(buttonsLayout)
        bottomLayout.addWidget(self.hairNodesList)

        # main layout, vertical
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottomLayout)

        self.setLayout(mainLayout)
        pass

    def readCache(self, fileName):
        # TODO read cache contents from specified file
        cacheFile = open(fileName, mode='r')
        self.cacheDict = json.load(cacheFile)
        cachefile.close()
        pass

    def appendAttribsToCache(self, cacheFile):
        # TODO append hair attribs to cache file
        pass

    def specifyCacheFile(self):
        # TODO specify the cache file
        cacheFileName = QtGui.QFileDialog.getOpenFileName(self, "select cache file", ".",  "*.*")
        self.fileNameLineEdit.setText(cacheFileName)
        pass

    def getCachedAttrib(self):
        # TODO get select attribute from cache file
        pass

    def writeCacheFile(self):
        # TODO write cache file
        pass

    def getAttribsFromSelectedHairNode(self):
        # TODO create a dict from Selected Hair Node
        pass

dlg = HairAttribCache()
dlg.show()
