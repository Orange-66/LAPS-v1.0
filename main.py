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

from Utils import app_info
from Utils import win_tool
from Window.win_index import Win_Index

if __name__ == "__main__":
    # 创建GUI应用程序
    app = QApplication(sys.argv)
    # 创建主窗体
    app_info.win_index = Win_Index()
    # 显示主窗体
    app_info.win_index.show()

    # 修饰窗体
    win_tool.center(app_info.win_index)
    win_tool.add_icon(app, app_info.logo_path)

    sys.exit(app.exec_())
