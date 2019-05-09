from UiFiles.Ui_MainLayout import Ui_MainLayout
from MyWidgets.FramelessWindow import FramelessWindow
from PyQt5.QtWidgets import QApplication,QWidget
import sys,os

class Do_MainLayout(QWidget,Ui_MainLayout):

    def __init__(self,*args,**kwargs):
        super(Do_MainLayout,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.setWindowTitle('测试')
        self._initUi()
    
    def _initUi(self):
        titleWidget=FramelessWindow()
        self.verticalLayout.addWidget(titleWidget)





if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=Do_MainLayout()
    w.show()
    sys.exit(app.exec_())