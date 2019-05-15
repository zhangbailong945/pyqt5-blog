from UiFiles.Ui_BottomOtherWidget import Ui_BottomOtherWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
import sys,os

class Do_BottomOtherWidget(QWidget,Ui_BottomOtherWidget):

    def __init__(self,*args,**kwargs):
        super(Do_BottomOtherWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self._initUi()
    
    def _initUi(self):
        self.resize(800,300)
        
