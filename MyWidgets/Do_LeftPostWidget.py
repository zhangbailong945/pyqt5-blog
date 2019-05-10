from UiFiles.Ui_LeftPostWidget import Ui_LeftPostWidget
from PyQt5.QtWidgets import QWidget
import sys,os

class Do_LeftPostWidget(QWidget,Ui_LeftPostWidget):

    def __init__(self,*args,**kwargs):
        super(Do_LeftPostWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self._initUi()
    
    def _initUi(self):
        self.resize(600,300)
        
