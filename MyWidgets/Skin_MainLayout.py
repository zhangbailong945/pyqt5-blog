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
from MyWidgets.Do_BottomTitleWidget import Do_BottomTitleWidget
from MyWidgets.Do_LeftCategoryWidget import Do_LeftCategoryWidget

from PyQt5.QtWidgets import QApplication,QWidget,QSpacerItem,QSizePolicy,QLabel
from PyQt5.QtGui import QEnterEvent,QFont,QFontDatabase,QPixmap,QColor
from PyQt5.QtCore import Qt,pyqtSignal,pyqtSlot,QEvent,QUrl,QTranslator,QLocale
from PyQt5.QtNetwork import QNetworkAccessManager,QNetworkReply,QNetworkRequest

from Utils.MyHttp import MyHttp
from Utils.Constants import Constants
from Utils.ThemeManager import ThemeManager
from Utils.CommonUtils import Setting
from Utils.GradientUtils import GradientUtils
from Utils.MyHttp import MyHttp
from Utils.CommonConstants import TranslationFile


import sys,os,json

class Skin_MainLayout(FramelessWindow,Ui_MainLayout):

    def __init__(self,*args,**kwargs):
        super(Skin_MainLayout,self).__init__(*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self._initLocalLanguage()
        self.setupUi(self)
        self.constants=Constants()
        self.font=ThemeManager.font()
        self._initUi()
        self._initIndex()
        self._initStyle()
        
    
    def _initLocalLanguage(self):
        if QLocale.system().language() in (QLocale.China,QLocale.Chinese,QLocale.Taiwan,QLocale.HongKong,QLocale.Macau):
            translator=QTranslator(self)
            translator.load(os.path.abspath(TranslationFile).replace('\\', '/'))
            QApplication.instance().installTranslator(translator)


    
    def _initStyle(self):
        colourful=Setting.value('colourful')
        if colourful:
            ThemeManager.loadFont()
            if isinstance(colourful,QColor):
                ThemeManager.loadColourfulTheme(colourful)
            else:
                # json数据转渐变
                ThemeManager.loadColourfulTheme(
                    GradientUtils.toGradient(colourful))
        else:
            ThemeManager.loadTheme()
    
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
        self.titleBar.pb_Skin.setText("\uf013")
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
        self.headerMenu.pb_Category.clicked.connect(self.on_pb_Category_clicked)
        self.headerMenu.pb_DateTime.clicked.connect(self.on_pb_DateTime_clicked)
        self.headerMenu.pb_Tags.clicked.connect(self.on_pb_Tags_clicked)
        self.headerMenu.pb_About.clicked.connect(self.on_pb_About_clicked)

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
        self.categoryHtmlPath=self.constants.path+"/MyWeb/category.html"
        self.tagsHtmlPath=self.constants.path+"/MyWeb/tags.html"
        self.tagsHtmlPath=self.constants.path+"/MyWeb/tags.html"
        self.aboutHtmlPath=self.constants.path+"/MyWeb/about.html"
        self.timeHtmlPath=self.constants.path+"/MyWeb/timeline.html"
        self.centerLeftPost.web_Post.load(QUrl("file:///"+self.indexHtmlPath))


        #分页面板
        self.centerLeftCategory=Do_LeftCategoryWidget()

        
        #左边
        self.vl_CenterLeft.addWidget(self.centerLeftPost)
        self.leftWidget.setContentsMargins(0,0,20,0)

        #右边
        self.vl_CenterRight.addWidget(self.centerRightLogin)
        self.vl_CenterRight.addSpacing(20)
        self.vl_CenterRight.addWidget(self.centerRightSearch)
        self.si_CenterRight=QSpacerItem(20,200,QSizePolicy.Minimum,QSizePolicy.Expanding)
        self.vl_CenterRight.addItem(self.si_CenterRight)
        

        #BottomWidget布局
        self.bottomTitle=Do_BottomTitleWidget()
        self.bottomOther=Do_BottomOtherWidget()
        self.bottomOther.setMinimumHeight(150)
        myHttp=MyHttp()
        bottomPostList=myHttp.getNewPostList()
        for p in bottomPostList:
            p['id']=QLabel("<html><head/><body><p><a href=\"https://loachblog.com/post/"+str(p['id'])+"/\"><span style=\" font-size:14px; color:#FFFFFF;text-decoration:none;\">"+p['title']+"</span></a></p></body></html>")
            p['id'].setOpenExternalLinks(True)
            self.bottomOther.verticalLayout.addWidget(p['id'])
        
        pmore=QLabel("<html><head/><body><p><a href=\"https://loachblog.com/\"><span style=\" font-size:14px; color:#FFFFFF;text-decoration:none;\">更多</span></a></p></body></html>")
        pmore.setOpenExternalLinks(True)
        self.bottomOther.verticalLayout.addWidget(pmore)
        self.bottomOther.widgetBottomLeft.setContentsMargins(10,10,10,10)
        self.bottomOther.verticalLayout.setSpacing(10)

        bottomTagList=myHttp.getNewTagList()
        for p in bottomTagList:
            p['id']=QLabel("<html><head/><body><p><a href=\"https://loachblog.com/tags/"+str(p['id'])+"/\"><span style=\" font-size:14px; color:#FFFFFF;text-decoration:none;\">"+p['name']+"</span></a></p></body></html>")
            p['id'].setOpenExternalLinks(True)
            self.bottomOther.verticalLayout_2.addWidget(p['id'])
        
        tmore=QLabel("<html><head/><body><p><a href=\"https://loachblog.com/\"><span style=\" font-size:14px; color:#FFFFFF;text-decoration:none;\">更多</span></a></p></body></html>")
        tmore.setOpenExternalLinks(True)
        self.bottomOther.verticalLayout_2.addWidget(tmore)
        self.bottomOther.widget_BottomCenter.setContentsMargins(10,10,10,10)


        #底部版权面板
        self.bottomCopyright=Do_BottomCopyrightWidget()
        self.bottomCopyright.setMinimumHeight(50)
        self.vl_Bottom.addWidget(self.bottomTitle)
        self.vl_Bottom.addWidget(self.bottomOther)
        self.vl_Bottom.addWidget(self.bottomCopyright)

    
    def eventFilter(self, obj, event):
        # 事件过滤器
        if obj == self.widgetMain and isinstance(event, QEnterEvent):
            # 用于解决鼠标进入其它控件后还原为标准鼠标样式
            self.setCursor(Qt.ArrowCursor)
        return FramelessWindow.eventFilter(self, obj, event)
    
    def on_pb_Category_clicked(self):
        self.centerLeftPost.web_Post.load(QUrl("file:///"+self.categoryHtmlPath))
    
    def on_pb_Index_clicked(self):
        self.centerLeftPost.web_Post.load(QUrl("file:///"+self.indexHtmlPath))
    
    def on_pb_DateTime_clicked(self):
        self.centerLeftPost.web_Post.load(QUrl("file:///"+self.timeHtmlPath))
    
    def on_pb_Tags_clicked(self):
        self.centerLeftPost.web_Post.load(QUrl("file:///"+self.tagsHtmlPath))
    
    def on_pb_About_clicked(self):
        self.centerLeftPost.web_Post.load(QUrl("file:///"+self.aboutHtmlPath))
    
    
    

    

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
        pass
    
    @pyqtSlot()
    def on_pb_pb_Maximum_clicked(self):
        '''
        最大化
        '''
        pass
        
    @pyqtSlot()
    def on_pb_Normal_clicked(self):
        """
        还原
        """
        pass
    
    @pyqtSlot()
    def on_pb_Close_clicked(self):
        """
        关闭
        """
        pass
    
    def changeEvent(self,event):
        #窗口改变改变事件
        pass
        
    def _initIndex(self):
        pass
    
if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=Skin_MainLayout()
    w.show()
    sys.exit(app.exec_())