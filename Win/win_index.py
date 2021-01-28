# -*- coding: utf-8 -*-
# @Time : 2021/1/22 5:01 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : win_index.py
# @Remark : 
# -----------------------------
import sys, random

from PyQt5.QtCore import pyqtSlot, Qt, QPointF

from PyQt5.QtGui import QBrush, QPolygonF, QPen, QFont, QTransform

from PyQt5.QtWidgets import (QApplication, QMainWindow, QColorDialog,
                             QFontDialog, QInputDialog, QLabel, QGraphicsScene,
                             QGraphicsView, QGraphicsItem, QGraphicsRectItem,
                             QGraphicsEllipseItem, QGraphicsPolygonItem,
                             QGraphicsLineItem, QGraphicsItemGroup, QGraphicsTextItem)

from PyUI.ui_index import Ui_Index
from Win.win_painting import Win_Painting
from Utils import app_info


class Win_Index(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_Index()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        # self.ui.btn_painting.clicked().connect(self.btn_painting_clicked)

    @pyqtSlot()
    def on_btn_painting_clicked(self):
        app_info.Win_Painting = Win_Painting()
        app_info.Win_Painting.show()


# ============窗体测试程序============
if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    win_index = Win_Index()  # 创建窗体
    win_index.show()
    sys.exit(app.exec_())
