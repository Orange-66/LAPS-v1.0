# -*- coding: utf-8 -*-
# @Time : 2021/1/22 5:01 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS
# @File : main.py
# @Remark : GUI应用程序主程序入口
# -----------------------------
import sys

from PyQt5.QtWidgets import QApplication

from Utils import settings
from Utils import tool_win
from Window.win_index import Win_Index

if __name__ == "__main__":
    # 创建GUI应用程序
    settings.app = QApplication(sys.argv)
    # 创建主窗体
    settings.win_index = Win_Index()
    # 显示主窗体
    settings.win_index.show()

    # 修饰窗体
    tool_win.center(settings.win_index)
    tool_win.add_icon(settings.logo_path)

    sys.exit(settings.app.exec_())
