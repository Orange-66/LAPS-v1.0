# -*- coding: utf-8 -*-
# @Time : 2021/1/22 10:41 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS
# @File : wid_canvas.py
# @Remark : 画布组件
# -----------------------------


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Utils import app_info
from Utils import win_tool


class Wid_Canvas(QWidget):
    # 绘画路径
    draw_path = []
    # 缓存路径
    tem_draw_path = []

    def __init__(self, parent=None):
        super().__init__(parent)
        self.finishPoint = QPoint()
        self.pen = QPen()
        self.pen.setWidth(app_info.pen_width)
        self.pen.setColor(app_info.pen_color)
        self.pix_back = QPixmap()
        self.init_ui()

    def init_ui(self):
        self.resize(600, 500)

        # 底层画布
        self.init_back()

    def init_back(self):
        self.pix_back = QPixmap(600, 500)  # 设置画布大小
        self.replace_back();

    # ========================事件函数========================
    # def keyPressEvent(self, event):
    #     # 前进操作
    #     if event.key() == Qt.Key_Y and QApplication.keyboardModifiers() == Qt.ControlModifier:
    #         self.forward()
    #
    #     # 后撤操作
    #     if event.key() == Qt.Key_Z and QApplication.keyboardModifiers() == Qt.ControlModifier:
    #         self.backward()

    # 绘图
    def paintEvent(self, event):
        self.replace_back()

        p = QPainter(self.pix_back)
        p.setPen(self.pen)
        self.draw(p)

        if self.hasMouseTracking():
            p.drawLine(self.draw_path[len(self.draw_path) - 1], self.finishPoint)

        p.drawPixmap(0, 0, self.pix_back)

        p = QPainter(self)
        p.drawPixmap(0, 0, self.pix_back)

    # 当鼠标左键按下时触发该函数
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.tem_draw_path.clear()
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

    # ========================自定义函数========================
    # 重绘背景图片
    def replace_back(self):
        self.pix_back.fill(Qt.white)  # 设置画布背景颜色为白色

        p = QPainter(self.pix_back)
        image = QPixmap(app_info.wid_canvas_image_path)
        p.drawPixmap(0, 0, 600, 500, image)

    # 绘制画笔痕迹
    def draw(self, painter, draw_path=draw_path):
        if len(self.draw_path) > 0:
            start = draw_path[0]
            for i in draw_path:
                finish = i
                painter.drawLine(start, finish)
                start = finish

    # 前进操作
    def forward(self):
        if len(self.tem_draw_path) > 0:
            pop_item = self.tem_draw_path.pop()
            self.draw_path.append(pop_item)
            self.update()
        else:
            print("前无可取")

    # 后撤操作
    def backward(self):
        if len(self.draw_path) > 0:
            pop_item = self.draw_path.pop()
            self.tem_draw_path.append(pop_item)
            self.update()
        else:
            print("后无可退")

    # 清除操作
    def clear(self):
        self.draw_path.clear()
        self.update()

    # 完成操作
    def done(self):
        self.pix_back
        painting_image = QImage()
        return painting_image


# ============窗体测试程序============
if __name__ == "__main__":
    win_tool.win_test(Wid_Canvas)
