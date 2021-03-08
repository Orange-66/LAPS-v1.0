# -*- coding: utf-8 -*-
# @Time : 2021/3/4 12:23 上午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : win_image_item.py
# @Remark : 
# -----------------------------
from PyQt5.QtWidgets import QWidget
from PyUI.ui_import_image import Ui_Import_Image


class Win_Image_Item(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.__ui = Ui_Import_Image()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面