# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Codes\PyQt5Projects\blogui\LeftPostWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets,QtWebEngineWidgets

class Ui_LeftPostWidget(object):



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

