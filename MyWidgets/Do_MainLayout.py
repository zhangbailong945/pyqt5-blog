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
from MyWidgets.Do_LeftCategoryWidget import Do_LeftCategoryWidget

from PyQt5.QtWidgets import QApplication,QWidget,QSpacerItem,QSizePolicy
from PyQt5.QtGui import QEnterEvent,QFont,QFontDatabase,QPixmap
from PyQt5.QtCore import Qt,pyqtSignal,pyqtSlot,QEvent,QUrl
from PyQt5.QtNetwork import QNetworkAccessManager,QNetworkReply,QNetworkRequest

from Utils.MyHttp import MyHttp
from Utils.Constants import Constants

import sys,os,json

class Do_MainLayout(FramelessWindow,Ui_MainLayout):

    def __init__(self,*args,**kwargs):
        super(Do_MainLayout,self).__init__(*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.constants=Constants()

        self.font=self.constants.myFont
        self._initUi()
        self._initIndex()
    
    def _initUi(self):
        self.resize(800,600)
        #TopWidget布局

        #1.标题栏面板
        self.titleBar=Do_HeaderTitlebarWidget()
        #连接按钮槽函数
        self.titleBar.pb_Close.clicked.connect(self.on_pb_Close_clicked)
        self.titleBar.pb_Skin.clicked.connect(self.on_pb_Skin_clicked)
        self.titleBar.pb_Minimum.clicked.connect(self.on_pb_Minimum_clicked)
        self.titleBar.pb_Maximum.clicked.connect(self.on_pb_pb_Maximum_clicked)
        self.titleBar.pb_Normal.clicked.connect(self.on_pb_Normal_clicked)
        
        #设置按钮图标
        self.titleBar.pb_Skin.setText("\uf0e4")
        self.titleBar.pb_Skin.setFont(self.font)
        self.titleBar.pb_Minimum.setText("\uf2d1")
        self.titleBar.pb_Minimum.setFont(self.font)
        self.titleBar.pb_Maximum.setText("\uf2d0")
        self.titleBar.pb_Maximum.setFont(self.font)
        self.titleBar.pb_Normal.setText("\uf2d2")
        self.titleBar.pb_Normal.setFont(self.font)
        self.titleBar.pb_Close.setText("\uf00d")
        self.titleBar.pb_Close.setFont(self.font)


        self.titleBar.pb_Normal.setVisible(False)

        #2.头像logo面板
        self.headerImg=Do_HeaderImgWidget()
        #设置头像logo
        self.headerImg.pb_HeaderImg.setPixmap(self.constants.myLogo)

        #3.文字面板
        self.headerText=Do_HeaderTextWidget()
        self.headerText.setMinimumHeight(50)
        self.headerText.lb_HeaderText1.setAlignment(Qt.AlignCenter)
        self.headerText.lb_HeaderText2.setAlignment(Qt.AlignCenter)

        #4.菜单面板
        self.headerMenu=Do_HeaderMenuWidget()
        self.headerMenu.setMaximumHeight(40)
        self.vl_Top.addWidget(self.titleBar)
        self.vl_Top.addWidget(self.headerImg)
        self.vl_Top.addWidget(self.headerText)
        self.vl_Top.addWidget(self.headerMenu)
        self.headerMenu.pb_Index.setChecked(True)
        self.headerMenu.pb_Category.clicked.connect(self.on_pb_Category_clicked)
        self.headerMenu.pb_Index.clicked.connect(self.on_pb_Index_clicked)


        #5.CenterWidget布局
        self.vl_Center.setStretch(3,1)
        self.vl_Center.setContentsMargins(35,35,35,35)

        #首页面板
        self.centerLeftPost=Do_LeftPostWidget()
        self.centerLeftPost.setAutoFillBackground(True)
        self.centerLeftPost.setAttribute(Qt.WA_StyledBackground,True)
        self.centerRightLogin=Do_RightLoginWidget()
        self.centerRightLogin.setAttribute(Qt.WA_StyledBackground,True)
        self.centerRightSearch=Do_RightSearchWidget()
        self.centerRightSearch.setAttribute(Qt.WA_StyledBackground,True)
        self.indexHtmlPath=self.constants.path+"/MyWeb/index.html"
        self.centerLeftPost.web_Post.load(QUrl("file:///"+self.indexHtmlPath))

        #分页面板
        self.centerLeftCategory=Do_LeftCategoryWidget()

        #self.vl_CenterLeft.addWidget(self.centerLeftPost)
        #左边
        self.leftWidget.addWidget(self.centerLeftPost)

        self.leftWidget.addWidget(self.centerLeftCategory)
        self.leftWidget.setContentsMargins(0,0,20,0)

        #右边
        self.vl_CenterRight.addWidget(self.centerRightLogin)
        self.vl_CenterRight.addSpacing(20)
        self.vl_CenterRight.addWidget(self.centerRightSearch)
        self.si_CenterRight=QSpacerItem(20,200,QSizePolicy.Minimum,QSizePolicy.Expanding)
        self.vl_CenterRight.addItem(self.si_CenterRight)
        

        #BottomWidget布局
        self.bottomOther=Do_BottomOtherWidget()
        self.bottomOther.setMinimumHeight(100)


        #底部版权面板
        self.bottomCopyright=Do_BottomCopyrightWidget()
        self.bottomCopyright.setMinimumHeight(50)
        
        self.vl_Bottom.addWidget(self.bottomOther)
        self.vl_Bottom.addWidget(self.bottomCopyright)
    
    def eventFilter(self, obj, event):
        # 事件过滤器
        if obj == self.widgetMain and isinstance(event, QEnterEvent):
            # 用于解决鼠标进入其它控件后还原为标准鼠标样式
            self.setCursor(Qt.ArrowCursor)
        return FramelessWindow.eventFilter(self, obj, event)
    
    def on_pb_Category_clicked(self):
        self.leftWidget.setCurrentIndex(1)
    
    def on_pb_Index_clicked(self):
        self.leftWidget.setCurrentIndex(0)
    

    @pyqtSlot()
    def on_pb_Skin_clicked(self):
        '''
        换皮肤
        '''
        pass

    @pyqtSlot()
    def on_pb_Minimum_clicked(self):
        '''
        最小化
        '''
        self.showMinimized()
    
    @pyqtSlot()
    def on_pb_pb_Maximum_clicked(self):
        '''
        最大化
        '''
        self.showMaximized()
        
    @pyqtSlot()
    def on_pb_Normal_clicked(self):
        """
        还原
        """
        self.showNormal()
    
    @pyqtSlot()
    def on_pb_Close_clicked(self):
        """
        关闭
        """
        self.close()
    
    def changeEvent(self,event):
        #窗口改变改变事件
        FramelessWindow.changeEvent(self,event)
        if event.type()==QEvent.WindowStateChange:
            state=self.windowState()
            if state==(state | Qt.WindowMaximized):
                #最大化状态显示还原按钮
                self.titleBar.pb_Maximum.setVisible(False)
                self.titleBar.pb_Normal.setVisible(True)
            else:
                #隐藏还原按钮
                self.titleBar.pb_Maximum.setVisible(True)
                self.titleBar.pb_Normal.setVisible(False)
        
    def _initIndex(self):
        pass
    
if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=Do_MainLayout()
    w.show()
    sys.exit(app.exec_())