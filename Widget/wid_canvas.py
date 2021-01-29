# -*- coding: utf-8 -*-
# @Time : 2020/12/28 12:55 下午
# @Author : Qi Tianyue
# @Email : qity_66@outlook.com
# @PROJECT : gui 
# @File : test.py


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Utils import app_info
from Utils import win_tool


class Wid_Canvas(QWidget):
    # 绘画路径
    draw_path = []

    def __init__(self, parent=None):
        super().__init__(parent)
        self.finishPoint = QPoint()

        self.pix_back = QPixmap()
        self.init_ui()

    def init_ui(self):
        self.resize(600, 500)

        # 底层画布
        self.init_back()

    def init_back(self):
        self.pix_back = QPixmap(600, 500)  # 设置画布大小
        self.replace_back();

    def replace_back(self):
        self.pix_back.fill(Qt.white)  # 设置画布背景颜色为白色

        p = QPainter(self.pix_back)
        image = QPixmap(app_info.wid_canvas_image_path)
        p.drawPixmap(0, 0, 600, 500, image)

    def keyPressEvent(self, event):
        # 撤销操作
        if event.key() == Qt.Key_Z and QApplication.keyboardModifiers() == Qt.ControlModifier:
            print("ctrl + z")

        # 取消撤销操作
        if event.key() == Qt.Key_Y and QApplication.keyboardModifiers() == Qt.ControlModifier:
            print("ctrl + y")

    def draw(self, painter, draw_path=draw_path):
        if len(self.draw_path) > 0:
            start = draw_path[0]
            for i in draw_path:
                finish = i
                painter.drawLine(start, finish)
                start = finish

    # 绘图
    def paintEvent(self, event):
        self.replace_back()

        p = QPainter(self.pix_back)
        self.draw(p)

        if self.hasMouseTracking():
            p.drawLine(self.draw_path[len(self.draw_path) - 1], self.finishPoint)

        p.drawPixmap(0, 0, self.pix_back)

        p = QPainter(self)
        p.drawPixmap(0, 0, self.pix_back)

    # 当鼠标左键按下时触发该函数
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.finishPoint = event.pos()
            self.draw_path.append(self.finishPoint)
            self.update()
            self.setMouseTracking(True)
        if event.button() == Qt.RightButton:
            self.setMouseTracking(False)

    # 当鼠标移动时触发该函数
    def mouseMoveEvent(self, event):
        self.finishPoint = event.pos()
        self.update()  # 调用paintEvent函数，重新绘制

    # 双击鼠标左键取消绘图
    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setMouseTracking(False)


# ============窗体测试程序============
if __name__ == "__main__":
    win_tool.win_test(Wid_Canvas)
