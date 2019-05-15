#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   CommonUtil.py
@Time    :   2019/05/15 11:00:53
@Author  :   Loach 
@Version :   1.0
@Contact :   1207549344@qq.com
@License :   (C)Copyright 2017-2019, loachblog.com
@Desc    :   共用工具
'''
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFont,QFontDatabase
import sys,os


class Constants(object):
    
    def __init__(self,*args,**kwargs):
        super(Constants,self).__init__(*args,**kwargs)
        self.path=os.path.abspath(os.path.dirname(os.path.dirname(__file__))).replace('\\','/')
        self.myFont=self.initFont()
        self.myLogo=self.initLogo()

    
    def initFont(self):
        """
        初始化字体
        """
        FontPath=self.path+"/Resources/Fonts/Font-Awesome-5-Free-Solid-900.otf"

        FontId=QFontDatabase.addApplicationFont(FontPath)
        FontFamilies=QFontDatabase.applicationFontFamilies(FontId)

        if len(FontFamilies)!=0:
            FontName=FontFamilies[0]
            return QFont(FontName,30)
        else:
            return None
    
    def initLogo(self):
        """
        初始化logo
        """
        return self.path+'/Resources/Images/logo.png'
        
        

