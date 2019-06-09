# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Codes\PyQt5Projects\blogui\LeftPostWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets,QtWebEngineWidgets

class Ui_LeftPostWidget(object):

    webPostStyle="""
/*QScrollBar Style*/

/*纵向滚动条*/
QScrollBar:vertical {
    background: transparent; /*背景透明*/
    width: 10px; /*宽度*/
    margin: 0px 0px 0px 0px; /**/
    padding-top: 12px; /*距离上面12px*/
    padding-bottom: 12px; /*距离底部12px*/
}
/*横向滚动条*/
QScrollBar:horizontal {
    background: transparent;
    height: 10px; /*高度*/
    margin: 0px 0px 0px 0px;
    padding-left: 12px; /*距离左边12px*/
    padding-right: 12px; /*距离右边12px*/
}

/*当鼠标放到纵向或者横向滚动条上面时*/
QScrollBar:vertical:hover,QScrollBar:horizontal:hover {
    background: rgba(0, 0, 0, 30); /*修改背景透明度 30*/
    border-radius: 5px; /*圆角*/
}

/*纵向滚动条上面的滑块*/
QScrollBar::handle:vertical {
    background: rgba(0, 0, 0, 50);
    width: 10px;
    border-radius: 5px;
    border: none;
}
/*横向滚动条上面的滑块*/
QScrollBar::handle:horizontal {
    background: rgba(0, 0, 0, 50);
    height: 10px;
    border-radius: 5px;
    border: none;
}

/*当鼠标放到滚动条滑块上面时改变透明度实现颜色的深浅变化*/
QScrollBar::handle:vertical:hover,QScrollBar::handle:horizontal:hover {
    background: rgba(0, 0, 0, 100);
}

/*纵向滚动条下部分块*/
QScrollBar::add-page:vertical {
    width: 10px;
    background: transparent;
}
/*横向滚动条后面部分块*/
QScrollBar::add-page:horizontal {
    height: 10px;
    background: transparent;
}
/*纵向滚动条上面部分块*/
QScrollBar::sub-page:vertical {
    width: 10px;
    background: transparent;
}
/*横向滚动条左部分块*/
QScrollBar::sub-page:horizontal {
    height: 10px;
    background: transparent;
}
/*纵向滚动条顶部三角形位置*/
QScrollBar::sub-line:vertical {
    height: 12px;
    width: 10px;
    background: transparent;
    subcontrol-position: top;
}
/*横向滚动条左侧三角形位置*/
QScrollBar::sub-line:horizontal {
    height: 10px;
    width: 12px;
    background: transparent;
    subcontrol-position: left;
}
/*纵向滚动条向上的三角形小图标*/
QScrollBar::up-arrow:vertical {
    image: url(../Resources/Images/scrollbar_arrowup_normal.png);
}
/*横向滚动条左边的三角形小图标*/
QScrollBar::left-arrow:horizontal {
    image: url(../Resources/Images/scrollbar_arrowleft_normal.png);
}
/*纵向滚动条向上的三角形小图标 鼠标悬停*/
QScrollBar::up-arrow:vertical:hover {
    image: url(../Resources/Images/scrollbar_arrowup_down.png);
}
/*横向滚动条左边的三角形小图标 鼠标悬停*/
QScrollBar::left-arrow:horizontal:hover {
    image: url(../Resources/Images/scrollbar_arrowleft_down.png);
}
/*纵向滚动条向上的三角形小图标 鼠标按下*/
QScrollBar::up-arrow:vertical:pressed {
    image: url(../Resources/Images/scrollbar_arrowup_highlight.png);
}
/*横向滚动条左边的三角形小图标 鼠标按下*/
QScrollBar::left-arrow:horizontal:pressed {
    image: url(../Resources/Images/scrollbar_arrowleft_highlight.png);
}

/*纵向滚动条下面三角形部分*/
QScrollBar::add-line:vertical {
    height: 12px;
    width: 10px;
    background: transparent;
    subcontrol-position: bottom;
}
/*横向滚动条右边的三角形部分*/
QScrollBar::add-line:horizontal {
    height: 10px;
    width: 12px;
    background: transparent;
    subcontrol-position: right;
}
/*纵向滚动条下面三角形图标*/
QScrollBar::down-arrow:vertical {
    image: url(../Resources/Images/scrollbar_arrowdown_normal.png);
}
/*横向滚动条右侧三角形图标*/
QScrollBar::right-arrow:horizontal {
    image: url(../Resources/Images/scrollbar_arrowright_normal.png);
}
/*纵向滚动条下面三角形图标 鼠标悬停*/
QScrollBar::down-arrow:vertical:hover {
    image: url(../Resources/Images/scrollbar_arrowdown_down.png);
}
/*横向滚动条右侧三角形图标 鼠标悬停*/
QScrollBar::right-arrow:horizontal:hover {
    image: url(../Resources/Images/scrollbar_arrowright_down.png);
}
/*纵向滚动条下面三角形图标 鼠标按下*/
QScrollBar::down-arrow:vertical:pressed {
    image: url(../Resources/Images/scrollbar_arrowdown_highlight.png);
}
/*横向滚动条右侧三角形图标 鼠标按下*/
QScrollBar::right-arrow:horizontal:pressed {
    image: url(../Resources/Images/scrollbar_arrowright_highlight.png);
}

    """

    def setupUi(self, LeftPostWidget):
        LeftPostWidget.setObjectName("LeftPostWidget")
        LeftPostWidget.resize(313, 208)
        LeftPostWidget.setAutoFillBackground(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(LeftPostWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.web_Post = QtWebEngineWidgets.QWebEngineView(LeftPostWidget)
        
        self.web_Post.setObjectName("web_Post")
        
        self.verticalLayout.addWidget(self.web_Post)

        self.retranslateUi(LeftPostWidget)
        QtCore.QMetaObject.connectSlotsByName(LeftPostWidget)

    def retranslateUi(self, LeftPostWidget):
        _translate = QtCore.QCoreApplication.translate
        LeftPostWidget.setWindowTitle(_translate("LeftPostWidget", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LeftPostWidget = QtWidgets.QWidget()
    ui = Ui_LeftPostWidget()
    ui.setupUi(LeftPostWidget)
    LeftPostWidget.show()
    sys.exit(app.exec_())

