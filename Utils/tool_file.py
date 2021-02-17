# -*- coding: utf-8 -*-
# @Time : 2021/1/24 3:47 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_file.py
# @Remark : 控制文件的工具类
# -----------------------------
from PyQt5.QtCore import QFile

from Utils import settings


def load_qss(qss_path):
    file = QFile(qss_path)
    file.open(QFile.ReadOnly)

    # QByteArray
    qt_bytes = file.readAll()
    # QByteArray转换为bytes
    py_bytes = qt_bytes.data()
    # bytes转换为str
    style_sheet = py_bytes.decode("utf-8")

    settings.app.setStyleSheet(style_sheet)
