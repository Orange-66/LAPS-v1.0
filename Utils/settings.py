# -*- coding: utf-8 -*-
# @Time : 2021/1/23 4:08 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : settings.py
# @Remark : 应用中各项参数
# -----------------------------
from PyQt5.QtGui import QColor
import logging


# -------------应用-------------
from PyQt5.QtSql import QSqlDatabase

app = None

# -------------路径-------------
# logo路径
# logo_path = "./Resource/Images/Icon/win_logo.ico"
logo_path = ":/icons/Images/Icon/win_logo.ico"
source_empty_image = "./Resource/Images/Png/sample_album/result/125-678ZFY-WSP-031720200317084921720.jpg"
# Mac路径
# wid_canvas_image_path = "/Users/orange/PycharmProjects/LAPS/Resource/Images/Png/wid_canvas_sample.png"

# Windows路径
# wid_canvas_image_path = "C:\\Users\\Orange\\PycharmProjects\\LAPS\\Resource\\Images\\Png\\wid_canvas_sample.png"

# -------------窗口-------------

win_index = None
win_painting = None
win_new_single = None
win_import_image = None
wid_preview = None
win_image_item = None

# -------------画笔-------------
pen_color = QColor(209, 26, 45)
pen_width = 2

# -------------画布-------------
canvas_width = 896
canvas_height = 392

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
                filename='./Docs/logging.txt',
                filemode='w')
# 日志记录开关
log.disable(log.DEBUG)

# -------------Excel-------------
# 工作表标题
excel_sheet_name = '患者基本信息表'
excel_sheet_titles = ['id', 'name', 'gender', 'age']
excel_file_name = '患者信息批量导入模版.xlsx'
excel_freeze_strategy = 'A2'
excel_title_width = 15
excel_font_size = 14
excel_bold = True
# -------------影像图片-------------
# 当前患者id
current_patient_id = None
# 当前患者name
current_patient_name = None
# 当前展示图片在列表中的坐标
image_index = 0
# 图片的id列表
image_id_list = []
# 当前患者的原始影像图片列表
original_image_list = []
# 当前患者的处理后影像图片列表
processed_image_list = []
# 当前患者的处理后影像图片列表的信息
processed_image_info_list = []
# 当前界面展示的原始影像图片
current_original_image = None
# 当前界面展示的处理后影像图片
current_processed_image = None
# -------------口口-------------
# -------------口口-------------
# -------------口口-------------
# -------------各个文件的所在地址-------------
# UI文件所在路径
ui_dir = '../UI/'
# qrc文件所在路径
qrc_dir = '../Resource/Qrc/'
# png文件所在路径
png_dir = '../Resource/Images/Png/'

# -------------各个文件的保存地址-------------
# ui to py文件保存路径-开发
ui_py_dir = '../PyUI/'
# ui to py文件保存路径-测试
ui_py_x_dir = '../PyUI-test/'
# qrc to py文件保存路径
qrc_py_dir = '../Resource/Qrc-py/'
# png to icon文件保存路径
png_icon_dir = '../Resource/Images/Icon/'
