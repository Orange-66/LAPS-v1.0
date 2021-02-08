# -*- coding: utf-8 -*-
# @Time : 2021/1/24 4:15 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_win.py
# @Remark : 控制窗口的工具类
# -----------------------------
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDesktopWidget, QApplication

from Utils import settings


# 添加窗口图标
def add_icon(icon_path):
    icon = QIcon(icon_path)
    settings.app.setWindowIcon(icon)


# 居中放置
def center(win):
    # 获取屏幕大小
    screen = QDesktopWidget().screenGeometry()
    # 获取窗口大小
    size = win.geometry()

    win.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


# 窗体测试
def win_test(window):
    app = QApplication(sys.argv)
    form = window()
    form.show()
    sys.exit(app.exec_())


# 关闭所有窗口，结束应用
def close_all():
    print("应用结束！")
    settings.app.exit()
