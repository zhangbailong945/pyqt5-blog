from UiFiles.Ui_BottomTitleWidget import Ui_BottomTitleWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
import sys,os

class Do_BottomTitleWidget(QWidget,Ui_BottomTitleWidget):

    def __init__(self,*args,**kwargs):
        super(Do_BottomTitleWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self._initUi()
    
    def _initUi(self):
        self.resize(800,300)
        
