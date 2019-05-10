from UiFiles.Ui_BottomCopyrightWidget import Ui_BottomCopyrightWidget
from PyQt5.QtWidgets import QWidget
import sys,os

class Do_BottomCopyrightWidget(QWidget,Ui_BottomCopyrightWidget):

    def __init__(self,*args,**kwargs):
        super(Do_BottomCopyrightWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self._initUi()
    
    def _initUi(self):
        self.resize(800,40)
        
