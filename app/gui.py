from .capture import Capture
from .ocr import OCR
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMargins, QTimer
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(872, 546)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # button
        self.screanshotbtm = QtWidgets.QPushButton(self.centralwidget)
        self.screanshotbtm.setGeometry(QtCore.QRect(770, 510, 91, 31))
        self.screanshotbtm.setObjectName("screanshotbtm")
        self.screanshotbtm.clicked.connect(self.captureWindows)
        self.screanshotbtm.setShortcut(QKeySequence("Ctrl+N"))

        # images
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 391, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.images = QtWidgets.QLabel(self.groupBox)
        self.images.setGeometry(QtCore.QRect(20, 20, 351, 441))
        self.images.setText("")
        self.images.setObjectName("images")
        self.verticalLayout.addWidget(self.groupBox)

        # texts
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(420, 20, 441, 481))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.texts = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.texts.setGeometry(QtCore.QRect(10, 20, 421, 451))
        self.texts.setObjectName("texts")
        self.verticalLayout_2.addWidget(self.groupBox_2)

        # show capture trigger
        self.capturetrigger = Capture()
        # initiate main windows
        self.windows = MainWindow
        # initiate OCR
        self.ocr = OCR()
        # set up file watcher for reload images
        self.pathImg = os.path.abspath('app/img/capture.png')
        self.file_watcher = QtCore.QFileSystemWatcher([self.pathImg])
        self.file_watcher.fileChanged.connect(self.loadImg)
        self.file_watcher.fileChanged.connect(self.loadOcr)
        self.loadOcr()
        self.loadImg()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.screanshotbtm.setText(_translate("MainWindow", "Screanshot"))
        self.groupBox.setTitle(_translate("MainWindow", "Images"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Text"))

    # run widget
    def captureWindows(self, MainWindow):
        self.capturetrigger.run(self.windows)

    # load image
    def loadImg(self):
        pathImg = QtGui.QPixmap(self.pathImg)
        if pathImg.isNull():
            pass
        else:
            self.images.setPixmap(pathImg)

    def loadOcr(self):
        pathImg = self.pathImg
        if pathImg:
            ocr_result = self.ocr.process_image(pathImg)
            self.texts.setPlainText(ocr_result)