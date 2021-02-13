# -*- coding: utf-8 -*-
# @Time : 2021/1/22 5:01 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : win_index.py
# @Remark : 主窗口
# -----------------------------
from PyQt5.QtCore import pyqtSlot, Qt, QItemSelectionModel
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAbstractItemView, QMessageBox)

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

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("./Resource/Database/laps.db")
        if self.db.open():
            self.qryModel = QSqlQueryModel(self)
            self.qryModel.setQuery('''SELECT state, id, name FROM patient_info ORDER BY id''')
            if self.qryModel.lastError().isValid():
                QMessageBox.warning(self, "错误", "数据表查询错误，出错消息\n" + self.qryModel.lastError().text())

            self.qryModel.setHeaderData(0, Qt.Horizontal, "状态")
            self.qryModel.setHeaderData(1, Qt.Horizontal, "编号")
            self.qryModel.setHeaderData(2, Qt.Horizontal, "姓名")

            self.selModel = QItemSelectionModel(self.qryModel)
            self.selModel.currentRowChanged.connect(self.do_currentRowChanged)

            self.__ui.table_patient_list.setModel(self.qryModel)
            self.__ui.table_patient_list.setSelectionModel(self.selModel)
        else:
            QMessageBox.warning(self, "错误", "打开数据库失败")

    def do_currentRowChanged(self, current, previous):
        if not current.isValid():
            return
        curRec = self.qryModel.record(current.row())
        id = curRec.value("id")
        self.qryModel_2 = QSqlQuery(self.db)
        self.qryModel_2.prepare('''SELECT * FROM patient_info WHERE id = :id ORDER BY id''')
        self.qryModel_2.bindValue(":id", id)
        if not self.qryModel_2.exec():
            QMessageBox.warning(self, "错误", "数据表查询错误，出错消息\n" + self.qryModel.lastError().text())
            return
        else:
            self.qryModel_2.first()

        tool_win.console_print(self.qryModel_2.value("name"))

        self.qryModel.setHeaderData(0, Qt.Horizontal, "状态")
        tool_win.console_print(id)

    # ========================重载事件函数========================
    def closeEvent(self, event):
        tool_win.close_all()
        tool_db.close_db()

    # ========================自动关联槽函数========================
    @pyqtSlot(bool)
    # 新建按钮-点击-槽函数
    def on_act_new_single_triggered(self):
        tool_win.console_print("on_btn_new_single_clicked")
        settings.Win_New_Single = Win_New_Single()
        settings.Win_New_Single.show()

    @pyqtSlot(bool)
    # 导入按钮-点击-槽函数
    def on_act_import_triggered(self):
        tool_win.console_print("on_btn_import_clicked")

    @pyqtSlot(bool)
    # 绘画按钮-点击-槽函数
    def on_act_painting_triggered(self):
        tool_win.console_print("on_btn_painting_clicked")
        settings.Win_Painting = Win_Painting()
        settings.Win_Painting.show()

    @pyqtSlot()
    # 上一张图片按钮-点击-槽函数
    def on_btn_up_page_clicked(self):
        tool_win.console_print("on_btn_up_page_clicked")

    @pyqtSlot()
    # 下一张图片按钮-点击-槽函数
    def on_btn_down_page_clicked(self):
        tool_win.console_print("on_btn_down_page_clicked")

    @pyqtSlot()
    # 图片信息按钮-点击-槽函数
    def on_btn_page_info_clicked(self):
        tool_win.console_print("on_btn_page_info_clicked")

    # ========================自定义函数========================
    # def __refresh_patient_list(self):
    #     tool_database


# ============窗体测试程序============
if __name__ == "__main__":  # 用于当前窗体测试
    tool_win.win_test(Win_Index)
