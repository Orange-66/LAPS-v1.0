# -*- coding: utf-8 -*-
# @Time : 2021/1/22 10:41 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS
# @File : wid_canvas.py
# @Remark : 画布组件
# -----------------------------
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Utils import settings, tool_win
from Utils import tool_log


class Wid_Canvas(QWidget):
    # 绘画路径
    painting_path = []
    # 缓存路径
    tem_painting_path = []
    # 设置画笔
    pen = QPen()
    pen.setWidth(settings.pen_width)
    pen.setColor(settings.pen_color_red)
    white_background = False

    def __init__(self, parent=None):
        super().__init__(parent)
        self.cursor_point = QPoint()

        self.resize(600, 1200)

        self.canvas = QPixmap(settings.canvas_width, settings.canvas_height)  # 设置画布大小
        self.canvas_clear()

    # ========================事件函数========================
    # 绘图事件
    def paintEvent(self, event):
        # 清空画布
        self.canvas_clear(self.white_background)

        painter = QPainter(self.canvas)
        painter.setPen(self.pen)

        if len(self.painting_path) > 1:
            start = self.painting_path[0]
            for i in self.painting_path:
                finish = i
                painter.drawLine(start, finish)
                start = finish

        if self.hasMouseTracking() and len(self.painting_path) > 0:
            painter.drawLine(self.painting_path[len(self.painting_path) - 1], self.cursor_point)

        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.canvas)

    # 当鼠标左键按下时触发该函数
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.tem_painting_path.clear()
            self.cursor_point = event.pos()
            self.painting_path.append(self.cursor_point)
            self.update()
            self.setMouseTracking(True)
        if event.button() == Qt.RightButton:
            self.setMouseTracking(False)

    # 当鼠标移动时触发该函数
    def mouseMoveEvent(self, event):
        self.cursor_point = event.pos()
        self.update()  # 调用paintEvent函数，重新绘制

    # 双击鼠标左键取消绘图
    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setMouseTracking(False)

    # ========================自定义函数========================
    # 重绘背景图片
    def canvas_clear(self, white_background=False):
        painter = QPainter(self.canvas)
        if white_background:
            rect = QRect(0, 0, settings.canvas_width, settings.canvas_height)
            painter.fillRect(rect, Qt.white)
        else:
            # canvas_image = QPixmap(settings.wid_canvas_image_path)
            canvas_image = settings.patient_image_list[settings.image_index]['original_image']
            painter.drawPixmap(0, 0, settings.canvas_width, settings.canvas_height, canvas_image)

    # 前进操作
    def forward(self):
        self.setMouseTracking(False)
        if len(self.tem_painting_path) > 0:
            if len(self.painting_path) == 0:
                pop_item = self.tem_painting_path.pop()
                self.painting_path.append(pop_item)
            pop_item = self.tem_painting_path.pop()
            self.painting_path.append(pop_item)
            self.update()
        else:
            tool_log.debug("forward, 前无可取")

    # 后撤操作
    def backward(self):
        self.setMouseTracking(False)
        if len(self.painting_path) > 0:
            if len(self.painting_path) == 2:
                pop_item = self.painting_path.pop()
                self.tem_painting_path.append(pop_item)
            pop_item = self.painting_path.pop()
            self.tem_painting_path.append(pop_item)
            self.update()
        else:
            tool_log.debug("forward, 后无可退")

    # 清除操作
    def clear(self):
        self.setMouseTracking(False)
        self.painting_path.clear()
        self.update()

    # 完成操作
    def done(self):
        self.setMouseTracking(False)
        self.white_background = True
        self.pen.setColor(settings.pen_color_black)
        self.paintEvent(None)
        self.white_background = False
        return self.canvas


# ============窗体测试程序============
if __name__ == "__main__":
    tool_win.win_test(Wid_Canvas)
