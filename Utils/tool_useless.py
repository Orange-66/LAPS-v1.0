# -*- coding: utf-8 -*-
# @Time : 2021/2/3 3:44 上午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_useless.py
# @Remark : 确实是无用的工具类
# -----------------------------
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication


def keyPressEvent(self, event):
    # 前进操作
    if event.key() == Qt.Key_Y and QApplication.keyboardModifiers() == Qt.ControlModifier:
        self.forward()

    # 后撤操作
    if event.key() == Qt.Key_Z and QApplication.keyboardModifiers() == Qt.ControlModifier:
        self.backward()