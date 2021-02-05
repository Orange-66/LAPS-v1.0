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
from Utils import app_info, tool_win
from Window.win_painting import Win_Painting


class Win_Index(QMainWindow, Ui_Index):
    album_index = 0
    album_list = []

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        # self.ui = Ui_Index()  # 创建UI对象
        self.setupUi(self)  # 构造UI界面

    @pyqtSlot()
    # 新建按钮-点击-槽函数
    def on_btn_new_clicked(self):
        print("on_btn_new_clicked")

    @pyqtSlot()
    # 导入按钮-点击-槽函数
    def on_btn_import_clicked(self):
        print("on_btn_import_clicked")

    @pyqtSlot()
    # 绘画按钮-点击-槽函数
    def on_btn_painting_clicked(self):
        print("on_btn_painting_clicked")
        app_info.Win_Painting = Win_Painting()
        app_info.Win_Painting.show()

    @pyqtSlot()
    # 上一张图片按钮-点击-槽函数
    def on_btn_up_page_clicked(self):
        print("on_btn_up_page_clicked")

    @pyqtSlot()
    # 下一张图片按钮-点击-槽函数
    def on_btn_down_page_clicked(self):
        print("on_btn_down_page_clicked")

    @pyqtSlot()
    # 图片信息按钮-点击-槽函数
    def on_btn_page_info_clicked(self):
        print("on_btn_page_info_clicked")


# ============窗体测试程序============
if __name__ == "__main__":  # 用于当前窗体测试
    tool_win.win_test(Win_Index)
