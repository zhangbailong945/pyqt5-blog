from UiFiles.Ui_MainLayout import Ui_MainLayout
from MyWidgets.FramelessWindow import FramelessWindow
from MyWidgets.Do_HeaderTitlebarWidget import Do_HeaderTitlebarWidget
from MyWidgets.Do_HeaderImgWidget import Do_HeaderImgWidget
from MyWidgets.Do_HeaderTextWidget import Do_HeaderTextWidget
from MyWidgets.Do_HeaderMenuWidget import Do_HeaderMenuWidget
from MyWidgets.Do_LeftPostWidget import Do_LeftPostWidget
from MyWidgets.Do_RightLoginWidget import Do_RightLoginWidget
from MyWidgets.Do_RightSearchWidget import Do_RightSearchWidget
from MyWidgets.Do_BottomOtherWidget import Do_BottomOtherWidget
from MyWidgets.Do_BottomCopyrightWidget import Do_BottomCopyrightWidget

from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QEnterEvent
from PyQt5.QtCore import Qt
import sys,os

class Do_MainLayout(FramelessWindow,Ui_MainLayout):

    def __init__(self,*args,**kwargs):
        super(Do_MainLayout,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self._initUi()
    
    def _initUi(self):
        self.resize(800,600)
        #TopWidget布局
        self.titleBar=Do_HeaderTitlebarWidget()
        self.headerImg=Do_HeaderImgWidget()
        self.headerText=Do_HeaderTextWidget()
        self.headerMenu=Do_HeaderMenuWidget()

        self.vl_Top.addWidget(self.titleBar)
        self.vl_Top.addWidget(self.headerImg)
        self.vl_Top.addWidget(self.headerText)
        self.vl_Top.addWidget(self.headerMenu)
        #CenterWidget布局
        self.centerLeftPost=Do_LeftPostWidget()
        self.centerRightLogin=Do_RightLoginWidget()
        self.centerRightSearch=Do_RightSearchWidget()

        self.vl_CenterLeft.addWidget(self.centerLeftPost)
        self.vl_CenterRight.addWidget(self.centerRightLogin)
        self.vl_CenterRight.addWidget(self.centerRightSearch)

        #BottomWidget布局
        self.bottomOther=Do_BottomOtherWidget()
        self.bottomCopyright=Do_BottomCopyrightWidget()
        
        self.vl_Bottom.addWidget(self.bottomOther)
        self.vl_Bottom.addWidget(self.bottomCopyright)
    
    def eventFilter(self, obj, event):
        # 事件过滤器
        if obj == self.widgetMain and isinstance(event, QEnterEvent):
            # 用于解决鼠标进入其它控件后还原为标准鼠标样式
            self.setCursor(Qt.ArrowCursor)
        return FramelessWindow.eventFilter(self, obj, event)













if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=Do_MainLayout()
    w.show()
    sys.exit(app.exec_())