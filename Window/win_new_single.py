# -*- coding: utf-8 -*-
# @Time : 2021/2/5 8:14 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : win_new_single.py
# @Remark : 新建病例-子窗口
# -----------------------------
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QApplication
from PyUI.ui_new_single import Ui_New_Single
from Utils import tool_win, app_info


class Win_New_Single(QWidget, Ui_New_Single):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.setupUi(self)  # 构造UI界面


# ============窗体测试程序============
if __name__ == "__main__":
    tool_win.win_test(Win_New_Single)
