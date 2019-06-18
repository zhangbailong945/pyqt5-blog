import hashlib
import logging
import os

from PyQt5.QtCore import QSettings, QTextCodec, QObject, pyqtSignal
from Utils.CommonConstants import ConfigFile



class Setting:

    _Setting = None

    @classmethod
    def init(cls, parent=None):
        """初始化配置实例
        :param cls:
        :param parent:
        """
        if not cls._Setting:
            cls._Setting = QSettings(ConfigFile, QSettings.IniFormat, parent)
            cls._Setting.setIniCodec(QTextCodec.codecForName('utf-8'))

    @classmethod
    def value(cls, key, default=None, typ=None):
        """获取配置中的值
        :param cls:
        :param key:        键名
        :param default:    默认值
        :param typ:        类型
        """
        cls.init()
        if default != None and typ != None:
            return cls._Setting.value(key, default, typ)
        if default != None:
            return cls._Setting.value(key, default)
        return cls._Setting.value(key)

    @classmethod
    def setValue(cls, key, value):
        """更新配置中的值
        :param cls:
        :param key:        键名
        :param value:      键值
        """
        cls.init()
        cls._Setting.setValue(key, value)
        cls._Setting.sync()


class _Signals(QObject):

    # 添加多彩item
    colourfulItemAdded = pyqtSignal(int, int, str, object)
    # 添加多彩item完成
    colourfulItemAddFinished = pyqtSignal()
    # 多彩item点击,色彩
    colourfulItemClicked = pyqtSignal(str, object)

# 说白了就是全局信号定义
Signals = _Signals()