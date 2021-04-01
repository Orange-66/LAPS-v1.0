# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI/ui_painting.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Painting(object):
    def setupUi(self, Painting):
        Painting.setObjectName("Painting")
        self.verticalLayout = QtWidgets.QVBoxLayout(Painting)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.wid_canvas = Wid_Canvas(Painting)
        Painting.resize(self.wid_canvas.height()+40, self.wid_canvas.width()+100)
        self.wid_canvas.setObjectName("wid_canvas")
        self.horizontalLayout_2.addWidget(self.wid_canvas)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(Painting)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_backward = QtWidgets.QPushButton(Painting)
        self.btn_backward.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_backward.setObjectName("btn_backward")
        self.horizontalLayout.addWidget(self.btn_backward)
        self.btn_forward = QtWidgets.QPushButton(Painting)
        self.btn_forward.setObjectName("btn_forward")
        self.horizontalLayout.addWidget(self.btn_forward)
        self.btn_clear = QtWidgets.QPushButton(Painting)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout.addWidget(self.btn_clear)
        self.btn_cancel = QtWidgets.QPushButton(Painting)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.btn_done = QtWidgets.QPushButton(Painting)
        self.btn_done.setStyleSheet("")
        self.btn_done.setObjectName("btn_done")
        self.horizontalLayout.addWidget(self.btn_done)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 9)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(Painting)
        QtCore.QMetaObject.connectSlotsByName(Painting)

    def retranslateUi(self, Painting):
        _translate = QtCore.QCoreApplication.translate
        Painting.setWindowTitle(_translate("Painting", "绘图"))
        self.btn_backward.setText(_translate("Painting", "< 后撤"))
        self.btn_backward.setShortcut(_translate("Painting", "Ctrl+Z"))
        self.btn_forward.setText(_translate("Painting", "前进 >"))
        self.btn_forward.setShortcut(_translate("Painting", "Ctrl+X"))
        self.btn_clear.setText(_translate("Painting", "清除"))
        self.btn_clear.setShortcut(_translate("Painting", "Ctrl+C"))
        self.btn_cancel.setText(_translate("Painting", "取消"))
        self.btn_done.setText(_translate("Painting", "完成"))
        self.btn_done.setShortcut(_translate("Painting", "Return"))
from Widget.wid_canvas import Wid_Canvas
