from UiFiles.Ui_HeaderImgWidget import Ui_HeaderImgWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
import sys,os

class Do_HeaderImgWidget(QWidget,Ui_HeaderImgWidget):

    def __init__(self,*args,**kwargs):
        super(Do_HeaderImgWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self._initUi()
    
    def _initUi(self):
        self.resize(800,100)
        