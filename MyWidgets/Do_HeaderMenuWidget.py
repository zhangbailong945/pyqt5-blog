from UiFiles.Ui_HeaderMenuWidget import Ui_HeaderMenuWidget
from PyQt5.QtWidgets import QWidget
import sys,os

class Do_HeaderMenuWidget(QWidget,Ui_HeaderMenuWidget):

    def __init__(self,*args,**kwargs):
        super(Do_HeaderMenuWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self._initUi()
    
    def _initUi(self):
        self.resize(800,40)
        
