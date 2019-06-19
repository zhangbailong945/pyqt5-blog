#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019年1月30日
@author: Irony
@site: https://pyqt5.com https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.Skins.PreviewWidget
@description: 主题预览
"""
import os

from PyQt5.QtCore import Qt, pyqtSlot, QTimer
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect

from UiFiles.Ui_MainLayout import Ui_MainLayout
from UiFiles.Ui_PreviewWidget import Ui_FormPreviewWidget
from Utils.CommonUtils import Setting
from Utils.GradientUtils import GradientUtils
from Utils.ThemeManager import ThemeManager


__Author__ = 'Irony'
__Copyright__ = 'Copyright (c) 2019'


class PreviewWidget(QWidget, Ui_FormPreviewWidget):

    Theme = 0
    Color = 1
    Picture = 2

    def __init__(self, *args, **kwargs):
        super(PreviewWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)  # 支持样式
        # 图片边缘阴影效果
        effect = QGraphicsDropShadowEffect(self.labelPreviewImage)
        effect.setBlurRadius(40)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.labelPreviewImage.setGraphicsEffect(effect)
        # 鼠标样式

    def setTitle(self, title):
        """设置标题
        :param title:
        """
        self.labelPreviewTitle.setText(title)
        self.setWindowTitle(title)

    def setPixmap(self, which, poc):
        """设置图片
        :param which:        Theme = 0,Color = 1,Picture = 2
        :param poc:          color or path
        """
        self._which = which
        self._poc = poc
        if not hasattr(self, '_UiMainWindow'):
            # 创建一个隐藏的主界面
            self._UiMainWindow = QWidget()
            ui = Ui_MainLayout()
            ui.setupUi(self._UiMainWindow)
            # 修改名字防止受app的style影响
            ui.setupUi().setObjectName('widgetMain1')
            self._UiMainWindow.setAttribute(Qt.WA_TranslucentBackground, True)
            self._UiMainWindow.setWindowFlags(
                self.windowFlags() | Qt.FramelessWindowHint)
            self._UiMainWindow.hide()
        if which == self.Theme:
            self.labelPreviewImage.setPixmap(
                QPixmap(poc).scaledToWidth(400, Qt.SmoothTransformation))
            return
        elif which == self.Color:
            ThemeManager.loadColourfulTheme(poc, self._UiMainWindow, {
                                            'widgetMain': 'widgetMain1'})
        # 对隐藏窗口截图
        # 至于为什么要加延迟, 设置样式后可能UI还没刷新
        self._UiMainWindow.repaint()
        QTimer.singleShot(100, self._updatePixmap)

    def _updatePixmap(self):
        poc = self._UiMainWindow.grab().scaledToWidth(400, Qt.SmoothTransformation)
        self.labelPreviewImage.setPixmap(poc)

    @pyqtSlot()
    def on_buttonPreviewClose_clicked(self):
        """隐藏自己
        """
        self.setVisible(False)

    @pyqtSlot()
    def on_buttonPreviewApply_clicked(self):
        """设置主题
        """
        if self._which == self.Theme:
            ThemeManager.loadUserTheme(
                os.path.basename(os.path.dirname(self._poc)))
            Setting.setValue('picture', None)
            Setting.setValue('colourful', None)
        elif self._which == self.Color:
            ThemeManager.loadColourfulTheme(self._poc)
            if isinstance(self._poc, QColor):
                Setting.setValue('colourful', self._poc)
            else:
                # 渐变需要转成字典数据
                Setting.setValue('colourful', GradientUtils.toJson(self._poc))
            Setting.setValue('picture', None)
