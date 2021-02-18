# -*- coding: utf-8 -*-
# @Time : 2021/1/22 5:01 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : win_index.py
# @Remark : 主窗口
# -----------------------------
from PyQt5.QtCore import pyqtSlot, Qt, QItemSelectionModel
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAbstractItemView, QMessageBox, QTableWidgetItem)

from PyUI.ui_index import Ui_Index
from Utils import settings, tool_win, tool_db
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
        self.__ui.table_patient_list.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.__ui.table_patient_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.__ui.table_patient_list.setAlternatingRowColors(True)
        self.__ui.table_patient_list.verticalHeader().hide()
        self.__ui.table_patient_list.verticalHeader().setDefaultSectionSize(22)
        self.__ui.table_patient_list.horizontalHeader().setDefaultSectionSize(53)

        self.__ui.table_image_info.setSpan(0, 0, 1, 4)
        self.__ui.table_image_info.setSpan(1, 1, 1, 3)

        item_title = QTableWidgetItem("患者基本信息", 1000)
        item_title.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.__ui.table_image_info.setItem(0, 0, item_title)


        # 查询并刷新患者列表
        self.query_model = tool_db.find_all()
        select_model = QItemSelectionModel(self.query_model)
        select_model.currentRowChanged.connect(self.do_currentRowChanged)

        self.__ui.table_patient_list.setModel(self.query_model)
        self.__ui.table_patient_list.setSelectionModel(select_model)

    def do_currentRowChanged(self, current, previous):
        if current.isValid():
            item_list = tool_db.find_by_id(self.query_model, current.row())
            if item_list is not None:
                self.__ui.table_image_info.setItem(1, 1, item_list[0])
                self.__ui.table_image_info.setItem(2, 1, item_list[1])
                self.__ui.table_image_info.setItem(2, 3, item_list[2])
                self.__ui.table_image_info.setItem(3, 1, item_list[3])
                self.__ui.table_image_info.setItem(3, 3, item_list[4])
                self.__ui.table_image_info.setItem(4, 1, item_list[5])
                self.__ui.table_image_info.setItem(4, 3, item_list[6])
                self.__ui.table_image_info.setItem(5, 1, item_list[7])
                self.__ui.table_image_info.setItem(5, 3, item_list[8])
                self.__ui.table_image_info.setItem(6, 1, item_list[9])
                self.__ui.table_image_info.setItem(6, 3, item_list[10])

    # ========================重载事件函数========================
    def closeEvent(self, event):
        tool_win.close_all()
        tool_db.close_db()

    # ========================自动关联槽函数========================
    @pyqtSlot(bool)
    # 新建按钮-点击-槽函数
    def on_act_new_single_triggered(self):
        tool_win.logging("on_btn_new_single_clicked")
        settings.Win_New_Single = Win_New_Single()
        settings.Win_New_Single.show()

    @pyqtSlot(bool)
    # 导入按钮-点击-槽函数
    def on_act_import_triggered(self):
        tool_win.logging("on_btn_import_clicked")

    @pyqtSlot(bool)
    # 绘画按钮-点击-槽函数
    def on_act_painting_triggered(self):
        tool_win.logging("on_btn_painting_clicked")
        settings.Win_Painting = Win_Painting()
        settings.Win_Painting.show()

    @pyqtSlot()
    # 上一张图片按钮-点击-槽函数
    def on_btn_up_page_clicked(self):
        tool_win.logging("on_btn_up_page_clicked")

    @pyqtSlot()
    # 下一张图片按钮-点击-槽函数
    def on_btn_down_page_clicked(self):
        tool_win.logging("on_btn_down_page_clicked")

    @pyqtSlot()
    # 图片信息按钮-点击-槽函数
    def on_btn_page_info_clicked(self):
        tool_win.logging("on_btn_page_info_clicked")

    # ========================自定义函数========================
    # def __refresh_patient_list(self):
    #     tool_database


# ============窗体测试程序============
if __name__ == "__main__":  # 用于当前窗体测试
    tool_win.win_test(Win_Index)
