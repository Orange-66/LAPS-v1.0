# -*- coding: utf-8 -*-
# @Time : 2021/1/22 10:41 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : win_painting.py
# @Remark : 绘画-子窗口
# -----------------------------
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QApplication
from PyUI.ui_painting import Ui_Painting
from Utils import tool_win, settings


class Win_Painting(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.__ui = Ui_Painting()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面

    # ========================自动关联槽函数========================
    @pyqtSlot()
    # 前进按钮-点击-槽函数
    def on_btn_forward_clicked(self):
        # tool_win.console_print("on_btn_forward_clicked")
        self.__ui.wid_canvas.forward()

    @pyqtSlot()
    # 后退按钮-点击-槽函数
    def on_btn_backward_clicked(self):
        # tool_win.console_print("on_btn_backward_clicked")
        self.__ui.wid_canvas.backward()

    @pyqtSlot()
    # 清除按钮-点击-槽函数
    def on_btn_clear_clicked(self):
        # tool_win.console_print("on_btn_clear_clicked")
        self.__ui.wid_canvas.clear()

    @pyqtSlot()
    # 完成按钮-点击-槽函数
    def on_btn_done_clicked(self):
        tool_win.console_print("on_btn_done_clicked")
        # return self.wid_canvas.done()

    @pyqtSlot()
    # 取消按钮-点击-槽函数
    def on_btn_cancel_clicked(self):
        # tool_win.console_print("on_btn_cancel_clicked")
        self.close()


# ============窗体测试程序============
if __name__ == "__main__":
    tool_win.win_test(Win_Painting)
