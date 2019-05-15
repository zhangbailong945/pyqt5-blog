# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Codes\PyQt5Projects\blogui\HeaderImgWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HeaderImgWidget(object):
    def setupUi(self, HeaderImgWidget):
        HeaderImgWidget.setObjectName("HeaderImgWidget")
        HeaderImgWidget.resize(400, 107)
        HeaderImgWidget.setAutoFillBackground(True)
        HeaderImgWidget.setStyleSheet("background-color: rgb(247, 155, 106);")
        self.hl_htw_img = QtWidgets.QHBoxLayout(HeaderImgWidget)
        self.hl_htw_img.setContentsMargins(0, 0, 0, 0)
        self.hl_htw_img.setSpacing(0)
        self.hl_htw_img.setObjectName("hl_htw_img")
        spacerItem = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hl_htw_img.addItem(spacerItem)
        self.lb_HeaderImg = QtWidgets.QLabel(HeaderImgWidget)
        self.lb_HeaderImg.setText("")
        self.lb_HeaderImg.setObjectName("lb_HeaderImg")
        self.hl_htw_img.addWidget(self.lb_HeaderImg)
        spacerItem1 = QtWidgets.QSpacerItem(143, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hl_htw_img.addItem(spacerItem1)

        self.retranslateUi(HeaderImgWidget)
        QtCore.QMetaObject.connectSlotsByName(HeaderImgWidget)

    def retranslateUi(self, HeaderImgWidget):
        _translate = QtCore.QCoreApplication.translate
        HeaderImgWidget.setWindowTitle(_translate("HeaderImgWidget", "Form"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HeaderImgWidget = QtWidgets.QWidget()
    ui = Ui_HeaderImgWidget()
    ui.setupUi(HeaderImgWidget)
    HeaderImgWidget.show()
    sys.exit(app.exec_())

