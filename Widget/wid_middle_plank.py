# -*- coding: utf-8 -*-
# @Time : 2021/2/10 1:07 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS
# @File : wid_middle_plank.py
# @Remark :
# -----------------------------
# QTableView组件的使用
from PyQt5.QtWidgets import QTableView, QHeaderView, QFormLayout, QVBoxLayout, QWidget, QApplication, QHBoxLayout, \
    QPushButton, QMainWindow, QGridLayout, QLabel
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from Utils import tool_win


class Wid_Middle_Plank(QWidget):

    def __init__(self, parent=None):
        super(Wid_Patient_Info, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.model = QStandardItemModel(13, 4)  # 存储任意结构数据
        # for row in range(13):
        #     for column in range(4):
        i = QStandardItem("日期")
        self.model.setItem(0, 0, i)
        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        self.tableView.verticalHeader().hide()
        self.tableView.horizontalHeader().hide()

        self.layout.addWidget(self.tableView)

        # 继承QMainWidow使用下面三行代码
        # widget=QWidget()
        # widget.setLayout(self.layout)
        # self.setCentralWidget(widget)

        # 继承QWidget则使用下面这样代码
        self.setLayout(self.layout)

        # 设置表格充满这个布局QHeaderView
        # self.tableView.horizontalHeader().setStretchLastSection(True)#最后一列决定充满剩下的界面
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面


if __name__ == "__main__":
    tool_win.win_test(Wid_Patient_Info)
