from UiFiles.Ui_HeaderTitlebarWidget import Ui_HeaderTitlebarWidget
from PyQt5.QtWidgets import QWidget
import sys,os

class Do_HeaderTitlebarWidget(QWidget,Ui_HeaderTitlebarWidget):

    def __init__(self,*args,**kwargs):
        super(Do_HeaderTitlebarWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self._initUi()
    
    def _initUi(self):
        self.resize(800,40)
        
