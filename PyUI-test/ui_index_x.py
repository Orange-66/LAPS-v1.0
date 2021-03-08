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
        Index.resize(858, 555)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Images/Icon/win_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Index.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Index)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_up_page = QtWidgets.QPushButton(self.frame)
        self.btn_up_page.setObjectName("btn_up_page")
        self.horizontalLayout_2.addWidget(self.btn_up_page)
        self.btn_page_info = QtWidgets.QPushButton(self.frame)
        self.btn_page_info.setObjectName("btn_page_info")
        self.horizontalLayout_2.addWidget(self.btn_page_info)
        self.btn_down_page = QtWidgets.QPushButton(self.frame)
        self.btn_down_page.setObjectName("btn_down_page")
        self.horizontalLayout_2.addWidget(self.btn_down_page)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 6)
        self.horizontalLayout_2.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_original_image = QtWidgets.QLabel(self.frame)
        self.label_original_image.setAutoFillBackground(False)
        self.label_original_image.setStyleSheet("background:rgb(255, 255, 255)")
        self.label_original_image.setText("")
        self.label_original_image.setObjectName("label_original_image")
        self.horizontalLayout_3.addWidget(self.label_original_image)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_processed_image = QtWidgets.QLabel(self.frame)
        self.label_processed_image.setStyleSheet("background:rgb(255, 255, 255)")
        self.label_processed_image.setText("")
        self.label_processed_image.setObjectName("label_processed_image")
        self.horizontalLayout_8.addWidget(self.label_processed_image)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(3, 5)
        self.frame_3 = QtWidgets.QFrame(self.splitter)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.graphics_left_image = QtWidgets.QGraphicsView(self.frame_3)
        self.graphics_left_image.setObjectName("graphics_left_image")
        self.horizontalLayout_4.addWidget(self.graphics_left_image)
        self.graphics_right_image = QtWidgets.QGraphicsView(self.frame_3)
        self.graphics_right_image.setObjectName("graphics_right_image")
        self.horizontalLayout_4.addWidget(self.graphics_right_image)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.table_image_info = QtWidgets.QTableWidget(self.frame_3)
        self.table_image_info.setAutoScroll(True)
        self.table_image_info.setObjectName("table_image_info")
        self.table_image_info.setColumnCount(4)
        self.table_image_info.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(8, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_image_info.setItem(10, 0, item)
        self.table_image_info.horizontalHeader().setVisible(False)
        self.table_image_info.verticalHeader().setVisible(False)
        self.verticalLayout_4.addWidget(self.table_image_info)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 9)
        self.frame_4 = QtWidgets.QFrame(self.splitter)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_search_bar = QtWidgets.QLineEdit(self.frame_4)
        self.line_search_bar.setObjectName("line_search_bar")
        self.verticalLayout_2.addWidget(self.line_search_bar)
        self.table_patient_list = QtWidgets.QTableView(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_patient_list.sizePolicy().hasHeightForWidth())
        self.table_patient_list.setSizePolicy(sizePolicy)
        self.table_patient_list.setMaximumSize(QtCore.QSize(160, 16777215))
        self.table_patient_list.setObjectName("table_patient_list")
        self.verticalLayout_2.addWidget(self.table_patient_list)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 9)
        self.horizontalLayout.addWidget(self.splitter)
        Index.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Index)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        Index.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(Index)
        self.toolBar.setIconSize(QtCore.QSize(25, 25))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        Index.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.act_new_single = QtWidgets.QAction(Index)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Root/Images/Png/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_new_single.setIcon(icon1)
        self.act_new_single.setObjectName("act_new_single")
        self.act_import = QtWidgets.QAction(Index)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Root/Images/Png/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_import.setIcon(icon2)
        self.act_import.setObjectName("act_import")
        self.act_painting = QtWidgets.QAction(Index)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Root/Images/Png/painting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_painting.setIcon(icon3)
        self.act_painting.setObjectName("act_painting")
        self.act_backward = QtWidgets.QAction(Index)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Root/Images/Png/backwark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_backward.setIcon(icon4)
        self.act_backward.setObjectName("act_backward")
        self.act_cancel = QtWidgets.QAction(Index)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Root/Images/Png/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_cancel.setIcon(icon5)
        self.act_cancel.setObjectName("act_cancel")
        self.act_delete = QtWidgets.QAction(Index)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Root/Images/Png/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_delete.setIcon(icon6)
        self.act_delete.setObjectName("act_delete")
        self.act_save = QtWidgets.QAction(Index)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Root/Images/Png/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_save.setIcon(icon7)
        self.act_save.setObjectName("act_save")
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.toolBar.addAction(self.act_new_single)
        self.toolBar.addAction(self.act_import)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_painting)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_backward)
        self.toolBar.addAction(self.act_cancel)
        self.toolBar.addAction(self.act_delete)
        self.toolBar.addAction(self.act_save)

        self.retranslateUi(Index)
        QtCore.QMetaObject.connectSlotsByName(Index)

    def retranslateUi(self, Index):
        _translate = QtCore.QCoreApplication.translate
        Index.setWindowTitle(_translate("Index", "LAP分析系统"))
        self.btn_up_page.setText(_translate("Index", "<"))
        self.btn_page_info.setText(_translate("Index", "第 NAN 张 / 共 NAN 张"))
        self.btn_down_page.setText(_translate("Index", ">"))
        item = self.table_image_info.verticalHeaderItem(0)
        item.setText(_translate("Index", "新建行"))
        item = self.table_image_info.verticalHeaderItem(1)
        item.setText(_translate("Index", "新建行"))
        item = self.table_image_info.verticalHeaderItem(2)
        item.setText(_translate("Index", "新建行"))
        item = self.table_image_info.verticalHeaderItem(3)
        item.setText(_translate("Index", "新建行"))
        item = self.table_image_info.verticalHeaderItem(4)
        item.setText(_translate("Index", "新建行"))
        item = self.table_image_info.verticalHeaderItem(5)
        item.setText(_translate("Index", "新建行"))
        item = self.table_image_info.verticalHeaderItem(6)
        item.setText(_translate("Index", "新建行"))
        item = self.table_image_info.verticalHeaderItem(7)
        item.setText(_translate("Index", "新建行"))
        item = self.table_image_info.verticalHeaderItem(8)
        item.setText(_translate("Index", "新建行"))
        item = self.table_image_info.verticalHeaderItem(9)
        item.setText(_translate("Index", "新建行"))
        item = self.table_image_info.verticalHeaderItem(10)
        item.setText(_translate("Index", "新建行"))
        item = self.table_image_info.horizontalHeaderItem(0)
        item.setText(_translate("Index", "新建列"))
        item = self.table_image_info.horizontalHeaderItem(1)
        item.setText(_translate("Index", "新建列"))
        item = self.table_image_info.horizontalHeaderItem(2)
        item.setText(_translate("Index", "新建列"))
        item = self.table_image_info.horizontalHeaderItem(3)
        item.setText(_translate("Index", "新建列"))
        __sortingEnabled = self.table_image_info.isSortingEnabled()
        self.table_image_info.setSortingEnabled(False)
        item = self.table_image_info.item(1, 0)
        item.setText(_translate("Index", "日期"))
        item = self.table_image_info.item(2, 0)
        item.setText(_translate("Index", "编号"))
        item = self.table_image_info.item(2, 2)
        item.setText(_translate("Index", "姓名"))
        item = self.table_image_info.item(3, 0)
        item.setText(_translate("Index", "性别"))
        item = self.table_image_info.item(3, 2)
        item.setText(_translate("Index", "年龄"))
        item = self.table_image_info.item(4, 0)
        item.setText(_translate("Index", "身高"))
        item = self.table_image_info.item(4, 2)
        item.setText(_translate("Index", "体重"))
        item = self.table_image_info.item(5, 0)
        item.setText(_translate("Index", "SBP"))
        item = self.table_image_info.item(5, 2)
        item.setText(_translate("Index", "DBP"))
        item = self.table_image_info.item(6, 0)
        item.setText(_translate("Index", "BSA"))
        item = self.table_image_info.item(6, 2)
        item.setText(_translate("Index", "BMI"))
        item = self.table_image_info.item(7, 0)
        item.setText(_translate("Index", "LAP"))
        item = self.table_image_info.item(7, 2)
        item.setText(_translate("Index", "TAU"))
        item = self.table_image_info.item(8, 1)
        item.setText(_translate("Index", "e"))
        item = self.table_image_info.item(8, 2)
        item.setText(_translate("Index", "a"))
        item = self.table_image_info.item(8, 3)
        item.setText(_translate("Index", "s"))
        item = self.table_image_info.item(9, 0)
        item.setText(_translate("Index", "MV"))
        item = self.table_image_info.item(10, 0)
        item.setText(_translate("Index", "IAS"))
        self.table_image_info.setSortingEnabled(__sortingEnabled)
        self.line_search_bar.setPlaceholderText(_translate("Index", "按下回车以搜索..."))
        self.menu.setTitle(_translate("Index", "LAPS"))
        self.menu_2.setTitle(_translate("Index", "设置"))
        self.menu_3.setTitle(_translate("Index", "帮助"))
        self.toolBar.setWindowTitle(_translate("Index", "toolBar"))
        self.act_new_single.setText(_translate("Index", "新建"))
        self.act_import.setText(_translate("Index", "导入"))
        self.act_painting.setText(_translate("Index", "绘图"))
        self.act_backward.setText(_translate("Index", "撤销"))
        self.act_cancel.setText(_translate("Index", "取消"))
        self.act_delete.setText(_translate("Index", "删除"))
        self.act_save.setText(_translate("Index", "保存"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Index = QtWidgets.QMainWindow()
    ui = Ui_Index()
    ui.setupUi(Index)
    Index.show()
    sys.exit(app.exec_())
