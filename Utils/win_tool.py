# -*- coding: utf-8 -*-
# @Time : 2021/1/24 4:15 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : win_tool.py
# @Remark : 控制窗口的工具类
# -----------------------------
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDesktopWidget


class Win_Tool:

    # 设置窗口图标
    @classmethod
    def add_icon(cls, app, icon_path):
        icon = QIcon(icon_path)
        app.setWindowIcon(icon)


    # 居中放置
    @classmethod
    def center(cls, win):
        # 获取屏幕大小
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口大小
        size = win.geometry()
        # print(size.width(), size.height(), screen.width(), screen.height())

        win.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
