# -*- coding: utf-8 -*-
# @Time : 2021/1/22 10:41 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : win_painting.py
# @Remark : 
# -----------------------------
import sys, random

from PyQt5.QtCore import pyqtSlot, Qt, QPointF

from PyQt5.QtGui import QBrush, QPolygonF, QPen, QFont, QTransform

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QColorDialog,
                             QFontDialog, QInputDialog, QLabel, QGraphicsScene,
                             QGraphicsView, QGraphicsItem, QGraphicsRectItem,
                             QGraphicsEllipseItem, QGraphicsPolygonItem,
                             QGraphicsLineItem, QGraphicsItemGroup, QGraphicsTextItem)

from PyUI.ui_painting import Ui_Painting


class Win_Painting(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_Painting()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面


# ============窗体测试程序============
if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = Win_Painting()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
