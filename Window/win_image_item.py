# -*- coding: utf-8 -*-
# @Time : 2021/3/4 12:23 上午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : win_image_item.py
# @Remark : 
# -----------------------------
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyUI.ui_image_item import Ui_Image_Item
from Utils import tool_db, tool_image, settings, tool_log


class Win_Image_Item(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.__ui = Ui_Image_Item()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面
        tool_image.set_image_by_label(
            settings.patient_image_list[settings.image_index]['uncropped_image'],
            self.__ui.label_image_item)

    @pyqtSlot()
    # 删除按钮-槽函数
    def on_btn_delete_clicked(self):
        tool_log.debug("on_btn_delete_clicked")
        tool_db.delete_current_image()
        settings.win_index.refresh_image_list()
