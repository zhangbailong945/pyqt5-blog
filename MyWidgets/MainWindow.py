from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot, QUrl, QLocale, QTranslator
from PyQt5.QtGui import QColor

from UiFiles.Ui_MainLayout import Ui_MainLayout
from MyWidgets.FramelessWindow import FramelessWindow
from MyWidgets.Do_MainLayout import Do_MainLayout

import sys,os

class MainWindow(FramelessWindow):

    def __init__(self,*args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)
        self._initUi()
    
    def _initUi(self):
        pass
    


if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWindow=MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())