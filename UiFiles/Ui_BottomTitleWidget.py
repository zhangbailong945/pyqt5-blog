# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\codes\PyQt5Projects\blogui\BottomTitleWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BottomTitleWidget(object):
    def setupUi(self, Ui_BottomTitleWidget):
        Ui_BottomTitleWidget.setObjectName("Ui_BottomTitleWidget")
        Ui_BottomTitleWidget.resize(959, 47)
        Ui_BottomTitleWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        Ui_BottomTitleWidget.setAutoFillBackground(False)
        Ui_BottomTitleWidget.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Ui_BottomTitleWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Ui_BottomTitleWidget)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Ui_BottomTitleWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 3))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("border-top:1px solid rgb(225,116, 43);margin-top:2px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(Ui_BottomTitleWidget)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(Ui_BottomTitleWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 3))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("border-top:1px solid rgb(225,116, 43);margin-top:2px;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(Ui_BottomTitleWidget)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(Ui_BottomTitleWidget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 3))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("border-top:1px solid rgb(225,116, 43);margin-top:2px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Ui_BottomTitleWidget)
        QtCore.QMetaObject.connectSlotsByName(Ui_BottomTitleWidget)

    def retranslateUi(self, Ui_BottomTitleWidget):
        _translate = QtCore.QCoreApplication.translate
        Ui_BottomTitleWidget.setWindowTitle(_translate("Ui_BottomTitleWidget", "Form"))
        self.label.setText(_translate("Ui_BottomTitleWidget", "New Posts"))
        self.label_3.setText(_translate("Ui_BottomTitleWidget", "New Tags"))
        self.label_5.setText(_translate("Ui_BottomTitleWidget", "Partners"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_BottomTitleWidget = QtWidgets.QWidget()
    ui = Ui_BottomTitleWidget()
    ui.setupUi(Ui_BottomTitleWidget)
    Ui_BottomTitleWidget.show()
    sys.exit(app.exec_())
