# -*- coding: utf-8 -*-
# @Time : 2021/1/23 4:08 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : settings.py
# @Remark : 应用中各项参数
# -----------------------------
from PyQt5.QtGui import QPixmap, QColor
import logging


# -------------应用-------------
from PyQt5.QtSql import QSqlDatabase

app = None

# -------------路径-------------
# logo路径
# logo_path = "./Resource/Images/Icon/win_logo.ico"
logo_path = ":/icons/Images/Icon/win_logo.ico"

# Mac路径
wid_canvas_image_path = "/Users/orange/PycharmProjects/LAPS/Resource/Images/Png/wid_canvas_sample.png"
# Windows路径
# wid_canvas_image_path = "C:\\Users\\Orange\\PycharmProjects\\LAPS\\Resource\\Images\\Png\\wid_canvas_sample.png"

# -------------窗口-------------

win_index = None
win_painting = None
win_new_single = None

# -------------画笔-------------

pen_color = QColor(209, 26, 45)
pen_width = 2

# -------------数据库-------------
# 数据库路径
db_path = "./Resource/Database/laps.db"
# 加载数据库驱动
db = QSqlDatabase.addDatabase("QSQLITE")
# 加载数据库文件
db.setDatabaseName(db_path)

# -------------日志-------------
log = logging
log.basicConfig(level=logging.DEBUG,
                format='%(asctime)s - %(levelname)s - %(message)s',
                filename='../Docs/logging.txt',
                filemode='w')
# 日志记录开关
# log.disable(log.DEBUG)

# -------------Excel-------------
# 工作表标题
excel_sheet_name = '患者基本信息表'
excel_sheet_titles = ['id', 'name', 'gender', 'age']
excel_file_name = '患者信息批量导入模版.xlsx'
excel_freeze_strategy = 'A2'
excel_title_width = 15
excel_font_size = 14
excel_bold = True
# -------------口口-------------
