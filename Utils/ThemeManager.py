import os

from PyQt5.QtGui import QFontDatabase,QCursor,QPixmap,QLinearGradient,\
    QRadialGradient,QConicalGradient
from PyQt5.QtWidgets import QApplication

from Utils.ColorThief import ColorThief
from Utils.GradientUtils import GradientUtils
from Utils.CommonUtils import Setting

#颜色模板
StyleColorTemplate="""
/*标题栏*/
#HeaderTitlebarWidget{
    background-color: rgba({0},{1},{2},255);
}
"""

StyleGradientTemplate="""
/*标题栏*/
#HeaderTitlebarWidget{
    background-color: rgba({0},{1},{2},255);
}
"""

class ThemeManager:

    ThemeDir='Resources/Themes'
    ThemeName='Default'

    @classmethod
    def styleSheet(cls):
        '''
        获取QApplication的样式
        '''
        return QApplication.instance().styleSheet()
    
    @classmethod
    def loadTheme(cls):
        ThemeManager.ThemeName=Setting.value('theme','Default',str)
        path=cls.fontPath()
        if os.path.isfile(path):
            QFontDatabase.addApplicationFont(path)
        path=cls.stylePath()
        try:
            QApplication.instance().setStyleSheet(
                open(path,'rb').read().decode('utf-8',errors='ignore')
            )
        except Exception as e:
            print(e)
    
    @classmethod
    def fontPath(cls):
        return os.path.abspath(os.path.join(ThemeManager.ThemeDir,ThemeManager.ThemeName,'font.ttf')).replace('\\','/')
    
    @classmethod
    def stylePath(cls,path=''):
        return os.path.abspath(os.path.join(ThemeManager.ThemeDir,path or ThemeManager.ThemeName,'style.qss')).replace('\\','/')



if __name__ == "__main__":
    print(ThemeManger.stylePath)