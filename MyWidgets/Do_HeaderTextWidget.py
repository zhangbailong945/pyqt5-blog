from UiFiles.Ui_HeaderTextWidget import Ui_HeaderTextWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
import sys,os

class Do_HeaderTextWidget(QWidget,Ui_HeaderTextWidget):

    def __init__(self,*args,**kwargs):
        super(Do_HeaderTextWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self._initUi()
    
    def _initUi(self):
        self.resize(800,50)
        