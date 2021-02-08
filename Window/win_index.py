# -*- coding: utf-8 -*-
# @Time : 2021/1/22 5:01 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : win_index.py
# @Remark : 主窗口
# -----------------------------
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAbstractItemView)

from PyUI.ui_index import Ui_Index
from Utils import settings, tool_win
from Utils import tool_db
from Window.win_painting import Win_Painting
from Window.win_new_single import Win_New_Single


class Win_Index(QMainWindow):
    album_index = 0
    album_list = []

    # ========================构造函数========================
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.__ui = Ui_Index()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面

        # table_patient_list的显示属性设置
        # self.__ui.table_patient_list.setSelectionBehavior(QAbstractItemView.SelectItems)
        # self.__ui.table_patient_list.setSelectionMode(QAbstractItemView.SingleSelection)
        # self.__ui.table_patient_list.setAlternatingRowColors(True)
        # self.__ui.table_patient_list.verticalHeader().setDefaultSectionSize(22)
        # self.__ui.table_patient_list.horizontalHeader().setDefaultSectionSize(60)
        #
        # tool_database.mapping("table_patient_list", self.__ui.table_patient_list)
    # ========================重载事件函数========================
    def closeEvent(self, event):
        tool_win.close_all()
        # tool_db.close()

    # ========================自动关联槽函数========================
    @pyqtSlot(bool)
    # 新建按钮-点击-槽函数
    def on_act_new_single_triggered(self):
        print("on_btn_new_single_clicked")
        settings.Win_New_Single = Win_New_Single()
        settings.Win_New_Single.show()

    @pyqtSlot(bool)
    # 导入按钮-点击-槽函数
    def on_act_import_triggered(self):
        print("on_btn_import_clicked")

    @pyqtSlot(bool)
    # 绘画按钮-点击-槽函数
    def on_act_painting_triggered(self):
        print("on_btn_painting_clicked")
        settings.Win_Painting = Win_Painting()
        settings.Win_Painting.show()

    @pyqtSlot()
    # 上一张图片按钮-点击-槽函数
    def on_btn_up_page_clicked(self):
        print("on_btn_up_page_clicked")

    @pyqtSlot()
    # 下一张图片按钮-点击-槽函数
    def on_btn_down_page_clicked(self):
        print("on_btn_down_page_clicked")

    @pyqtSlot()
    # 图片信息按钮-点击-槽函数
    def on_btn_page_info_clicked(self):
        print("on_btn_page_info_clicked")

    # ========================自定义函数========================
    # def __refresh_patient_list(self):
    #     tool_database


# ============窗体测试程序============
if __name__ == "__main__":  # 用于当前窗体测试
    tool_win.win_test(Win_Index)
