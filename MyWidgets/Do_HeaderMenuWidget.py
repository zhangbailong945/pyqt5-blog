from UiFiles.Ui_HeaderMenuWidget import Ui_HeaderMenuWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
import sys,os

class Do_HeaderMenuWidget(QWidget,Ui_HeaderMenuWidget):

    def __init__(self,*args,**kwargs):
        super(Do_HeaderMenuWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self._initUi()
    
    def _initUi(self):
        self.resize(800,40)
        
