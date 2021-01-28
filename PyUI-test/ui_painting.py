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
        Painting.resize(523, 371)
        self.verticalLayout = QtWidgets.QVBoxLayout(Painting)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Painting)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Canvas = QtWidgets.QGraphicsView(Painting)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout_2.addWidget(self.Canvas)
        self.horizontalLayout_2.setStretch(0, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spin_proportion = QtWidgets.QSpinBox(Painting)
        self.spin_proportion.setObjectName("spin_proportion")
        self.horizontalLayout.addWidget(self.spin_proportion)
        self.pushButton_3 = QtWidgets.QPushButton(Painting)
        self.pushButton_3.setMaximumSize(QtCore.QSize(78, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.btn_brush = QtWidgets.QPushButton(Painting)
        self.btn_brush.setObjectName("btn_brush")
        self.horizontalLayout.addWidget(self.btn_brush)
        self.btn_undo = QtWidgets.QPushButton(Painting)
        self.btn_undo.setObjectName("btn_undo")
        self.horizontalLayout.addWidget(self.btn_undo)
        self.image_next_button = QtWidgets.QPushButton(Painting)
        self.image_next_button.setObjectName("image_next_button")
        self.horizontalLayout.addWidget(self.image_next_button)
        self.pushButton_2 = QtWidgets.QPushButton(Painting)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Painting)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Painting)
        QtCore.QMetaObject.connectSlotsByName(Painting)

    def retranslateUi(self, Painting):
        _translate = QtCore.QCoreApplication.translate
        Painting.setWindowTitle(_translate("Painting", "绘图"))
        self.label.setText(_translate("Painting", "第 3 张 / 共 7 张"))
        self.pushButton_3.setText(_translate("Painting", "<"))
        self.btn_brush.setText(_translate("Painting", "画笔"))
        self.btn_undo.setText(_translate("Painting", "撤销"))
        self.image_next_button.setText(_translate("Painting", ">"))
        self.pushButton_2.setText(_translate("Painting", "取消"))
        self.pushButton.setText(_translate("Painting", "确认"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Painting = QtWidgets.QWidget()
    ui = Ui_Painting()
    ui.setupUi(Painting)
    Painting.show()
    sys.exit(app.exec_())
