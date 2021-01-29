# -*- coding: utf-8 -*-
# @Time : 2021/1/22 10:41 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : win_painting.py
# @Remark : 
# -----------------------------
import sys

from PyQt5.QtWidgets import (QApplication, QWidget)

from PyUI.ui_painting import Ui_Painting
from Utils import win_tool


class Win_Painting(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_Painting()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面


# ============窗体测试程序============
if __name__ == "__main__":
    win_tool.win_test(Win_Painting)
