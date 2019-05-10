from UiFiles.Ui_RightSearchWidget import Ui_RightSearchWidget
from PyQt5.QtWidgets import QWidget
import sys,os

class Do_RightSearchWidget(QWidget,Ui_RightSearchWidget):

    def __init__(self,*args,**kwargs):
        super(Do_RightSearchWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self._initUi()
    
    def _initUi(self):
        self.resize(200,300)
        
