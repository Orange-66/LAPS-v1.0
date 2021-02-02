# -*- coding: utf-8 -*-
# @Time : 2021/1/22 5:01 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : win_index.py
# @Remark : 主窗口
# -----------------------------
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QMainWindow)

from PyUI.ui_index import Ui_Index
from Utils import app_info, win_tool
from Window.win_painting import Win_Painting


class Win_Index(QMainWindow, Ui_Index):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        # self.ui = Ui_Index()  # 创建UI对象
        self.setupUi(self)  # 构造UI界面

    @pyqtSlot()
    # 绘画按钮-点击-槽函数
    def on_btn_painting_clicked(self):
        app_info.Win_Painting = Win_Painting()
        app_info.Win_Painting.show()


# ============窗体测试程序============
if __name__ == "__main__":  # 用于当前窗体测试
    win_tool.win_test(Win_Index)
