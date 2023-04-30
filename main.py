from app.capture import Capture
from app.gui import Ui_MainWindow
from PyQt5 import QtWidgets
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    # app = QtWidgets.QApplication(sys.argv)
    # window = Capture()
    # window.show()
    # app.aboutToQuit.connect(app.deleteLater)
    # sys.exit(app.exec_())
