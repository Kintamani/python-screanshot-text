import sys
import tkinter as tk
import numpy as np
import cv2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PIL import ImageGrab

class Capture(QtWidgets.QWidget):
    def __init__(self, main=None):
        super().__init__()
        # initiate main window
        self.main = main
        # self.main.loadImg(QtGui.QPixmap('path/to/image.png'))

        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # Get screen size
        screen_size  = tk.Tk()

        # Set window properties
        self.setGeometry(0, 0, screen_size.winfo_screenwidth(), screen_size.winfo_screenheight())
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.1)
        self.num_snip = 0
        self.is_snipping = False

        # Set cursor to crosshair
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
    
    # run windget
    def run(self, MainWindow):
        # Change value variable
        self.main = MainWindow
        self.main.close()
        
        # Set window to be frameless and display it
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        print('Capture the screen...')
        print('Press q if you want to quit...')
        self.show()

    # capture screan
    def paintEvent(self, event):
        if self.is_snipping:
            brush_color = (0, 0, 0, 0)
            lw = 0
            opacity = 0
        else:
            brush_color = (103, 103, 103, 128)
            lw = 1
            opacity = 0.1

        # Set window color when capture
        bg_color = QtGui.QColor(*brush_color)
        self.setStyleSheet("background-color: {}".format(bg_color.name()))
        self.setWindowOpacity(opacity)

        # Set rectangle when capture
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('white'), lw))
        qp.setBrush(QtGui.QColor(*brush_color))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    # event when key press
    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    # event when cursor press and move
    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    # event when cursor press release
    def mouseReleaseEvent(self, event):
        # Get the coordinates of the selected area
        x1, y1 = min(self.begin.x(), self.end.x()), min(self.begin.y(), self.end.y())
        x2, y2 = max(self.begin.x(), self.end.x()), max(self.begin.y(), self.end.y())

        # Indicate that the application is snipping
        self.is_snipping = True
        self.repaint()
        QtWidgets.QApplication.processEvents()
        
        # Capture the selected area
        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        
        # Indicate that the application has stopped snipping
        self.is_snipping = False
        self.repaint()
        QtWidgets.QApplication.processEvents()
        
        # Save the captured image to file
        img_name = 'app/img/capture.png'
        img.save(img_name)
        
        # Convert the image to RGB format using OpenCV
        # print(img_name, 'saved')
        img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

        # Quit event
        self.close()
        self.main.show()