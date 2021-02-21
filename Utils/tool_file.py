# -*- coding: utf-8 -*-
# @Time : 2021/1/24 3:47 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_file.py
# @Remark : 控制文件的工具类
# -----------------------------
import os
import zipfile
import openpyxl
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter
from PyQt5.QtCore import QFile, Qt

from Utils import settings, tool_win

# 加载qss文件
from Window.win_index import Win_Index


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


# 加载Excel文件
def load_excel(file_path):
    return openpyxl.load_workbook(file_path)


# 得到第一个工作表
def get_worksheet_by_index(work_book, index):
    sheet_names = work_book.get_sheet_names()
    work_sheet = work_book.get_sheet_by_names(sheet_names[index])
    return work_sheet


# 获取指定一行数据
def get_row_by_index(work_sheet, index):
    return work_sheet.row[index]


# 获取最大数据行数
def get_range_row(work_sheet):
    return range(2, work_sheet.get_highest_row())


# 创建一个excel文档
def create_sample(save_dir):
    # 获取excel实例对象
    work_book = openpyxl.Workbook()

    # 设置工作表名
    sheet_name = work_book.get_sheet_names()[0]
    sheet = work_book.get_sheet_by_name(sheet_name)
    sheet.title = settings.excel_sheet_name

    # 设置标题样式
    title_style = Font(size=settings.excel_font_size, bold=settings.excel_bold)

    # 冻结表头
    sheet.freeze_panes = settings.excel_freeze_strategy

    # 填写表头
    for i in range(len(settings.excel_sheet_titles)):
        column = get_column_letter(i + 1)
        # 设置表头样式以及内容
        sheet[column + '1'].font = title_style
        sheet[column + '1'] = settings.excel_sheet_titles[i]
        # 设置表头的宽
        sheet.column_dimensions[column].width = settings.excel_title_width

    # 保存excel表与指定位置
    work_book.save(os.path.join(save_dir, settings.excel_file_name))


# 打开图片文件
def open_image(window):
    image_name, _ = QFileDialog.getOpenFileName(window, "Open Image File", "*.jpg;;*.png;;*.jpeg")
    tool_win.logging(image_name)
    image_pix = QPixmap(image_name)
    return image_name, image_pix


# 根据文件路径截取文件名
def get_file_name(file_path):
    file_name = file_path.split(os.sep)[-1]
    tool_win.logging("get_file_name", file_path, file_name)
    return file_name
