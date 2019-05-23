from UiFiles.Ui_RightLoginWidget import Ui_RightLoginWidget
from PyQt5.QtWidgets import QWidget
import sys,os

class Do_RightLoginWidget(QWidget,Ui_RightLoginWidget):

    def __init__(self,*args,**kwargs):
        super(Do_RightLoginWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self._initUi()
    
    def _initUi(self):
        self.setMaximumHeight(120)
        self.setMinimumHeight(120)
        
