# -*- coding: utf-8 -*-
# @Time : 2021/1/24 3:47 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_file.py
# @Remark : 控制文件的工具类
# -----------------------------
import zipfile

from PyQt5.QtCore import QFile

from Utils import settings


# 加载qss文件
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


# 压缩文件
def compress_file():
    filename = "Laps.zip"
    zip_item = zipfile.ZipFile(filename, 'w')
    zip_item.write('./EXE', compress_type=zipfile.ZIP_DEFLATED)
    zip_item.close()
