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
from Utils.win_tool import Win_Tool
from Win.win_index import Win_Index

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建GUI应用程序
    win_main = Win_Index()  # 创建主窗体
    win_main.show()  # 显示主窗体
    Win_Tool.center(win_main)
    Win_Tool.add_icon(app, app_info.logo_path)
    win_painting = None

    sys.exit(app.exec_())
