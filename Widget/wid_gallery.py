# -*- coding: utf-8 -*-
# @Time : 2021/2/18 12:45 上午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : wid_gallery.py
# @Remark : 
# -----------------------------
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTableWidget, QTableWidgetItem

from PyUI.ui_image_item import Ui_Image_Item
from Utils import tool_win


class Wid_Gallery(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # self.resize(300, 500)

        # self.__ui = Ui_Wid_Image_Item()
        # self.__ui.setupUi(self)

        self.initUI()

    def initUI(self):
        self.resize(600, 500)
        conLayout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(1)
        tableWidget.setColumnCount(3)
        conLayout.addWidget(tableWidget)

        image_item = QTableWidgetItem(Ui_Image_Item())
        tableWidget.setCellWidget(0, 0, image_item)

        self.setLayout(conLayout)


# ============窗体测试程序============
if __name__ == "__main__":
    tool_win.win_test(Wid_Gallery)
