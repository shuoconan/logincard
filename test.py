import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from frameui import Ui_MainWindow
from login_frame import Ui_Dialog

class main_frame(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(main_frame,self).__init__()
        self.setupUi(self)
class login_frame(QMainWindow,Ui_Dialog):
    def __init__(self):
        super(login_frame,self).__init__()
        self.setupUi(self)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget =main_frame()
    widget.show()
    sys.exit(app.exec())