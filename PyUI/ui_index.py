# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI/ui_index.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Index(object):
    def setupUi(self, Index):
        Index.setObjectName("Index")
        Index.resize(812, 555)
        self.centralwidget = QtWidgets.QWidget(Index)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.new_button = QtWidgets.QPushButton(self.centralwidget)
        self.new_button.setObjectName("new_button")
        self.horizontalLayout.addWidget(self.new_button)
        self.import_button = QtWidgets.QPushButton(self.centralwidget)
        self.import_button.setObjectName("import_button")
        self.horizontalLayout.addWidget(self.import_button)
        self.btn_painting = QtWidgets.QPushButton(self.centralwidget)
        self.btn_painting.setObjectName("btn_painting")
        self.horizontalLayout.addWidget(self.btn_painting)
        self.zoom_button = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_button.setObjectName("zoom_button")
        self.horizontalLayout.addWidget(self.zoom_button)
        self.retrieval_button = QtWidgets.QPushButton(self.centralwidget)
        self.retrieval_button.setObjectName("retrieval_button")
        self.horizontalLayout.addWidget(self.retrieval_button)
        self.label_button = QtWidgets.QPushButton(self.centralwidget)
        self.label_button.setObjectName("label_button")
        self.horizontalLayout.addWidget(self.label_button)
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.lock_button = QtWidgets.QPushButton(self.centralwidget)
        self.lock_button.setObjectName("lock_button")
        self.horizontalLayout.addWidget(self.lock_button)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.image_info_button = QtWidgets.QPushButton(self.frame)
        self.image_info_button.setObjectName("image_info_button")
        self.horizontalLayout_8.addWidget(self.image_info_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.image_last_button = QtWidgets.QPushButton(self.frame)
        self.image_last_button.setObjectName("image_last_button")
        self.horizontalLayout_2.addWidget(self.image_last_button)
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_2.addWidget(self.graphicsView)
        self.image_next_button = QtWidgets.QPushButton(self.frame)
        self.image_next_button.setObjectName("image_next_button")
        self.horizontalLayout_2.addWidget(self.image_next_button)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 10)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.frame_2)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_3.addWidget(self.graphicsView_2)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.frame_3)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.horizontalLayout_4.addWidget(self.graphicsView_3)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.frame_3)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.horizontalLayout_4.addWidget(self.graphicsView_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 10)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_7.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textEdit = QtWidgets.QTextEdit(self.frame_4)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_5.addWidget(self.textEdit)
        self.listWidget = QtWidgets.QListWidget(self.frame_4)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_5.addWidget(self.listWidget)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 11)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_7.addWidget(self.frame_4)
        self.horizontalLayout_7.setStretch(0, 8)
        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(2, 2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        Index.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Index)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        Index.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Index)
        self.statusbar.setObjectName("statusbar")
        Index.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(Index)
        QtCore.QMetaObject.connectSlotsByName(Index)

    def retranslateUi(self, Index):
        _translate = QtCore.QCoreApplication.translate
        Index.setWindowTitle(_translate("Index", "LAP分析系统"))
        self.new_button.setText(_translate("Index", "新建"))
        self.import_button.setText(_translate("Index", "导入"))
        self.btn_painting.setText(_translate("Index", "绘图"))
        self.zoom_button.setText(_translate("Index", "缩放"))
        self.retrieval_button.setText(_translate("Index", "检索"))
        self.label_button.setText(_translate("Index", "标记"))
        self.delete_button.setText(_translate("Index", "删除"))
        self.lock_button.setText(_translate("Index", "锁定"))
        self.image_info_button.setText(_translate("Index", "第 3 张 / 共 7 张"))
        self.image_last_button.setText(_translate("Index", "<"))
        self.image_next_button.setText(_translate("Index", ">"))
        self.menu.setTitle(_translate("Index", "LAPS"))
        self.menu_2.setTitle(_translate("Index", "设置"))
        self.menu_3.setTitle(_translate("Index", "帮助"))
