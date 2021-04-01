# -*- coding: utf-8 -*-
# @Time : 2021/2/21 10:31 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : wid_preview.py
# @Remark : 
# -----------------------------
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget

from Utils import tool_win


class Wid_Preview(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.setWindowTitle("预览")


# ============窗体测试程序============
if __name__ == "__main__":
    tool_win.win_test(Wid_Preview)
