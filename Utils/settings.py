# -*- coding: utf-8 -*-
# @Time : 2021/1/23 4:08 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : settings.py
# @Remark : 应用中各项参数
# -----------------------------
from PyQt5.QtGui import QColor
from PyQt5.QtSql import QSqlDatabase

# -------------应用-------------
app = None

# -------------路径-------------
# 本地静态资源的路径用path
# logo路径
# logo_path = "./Resource/Images/Icon/win_logo.ico"
logo_path = ":/icons/Images/Icon/win_logo.ico"
source_empty_image = "Resource/Images/Background/empty_image.png"
source_empty_right_image = "Resource/Images/Background/empty_image.png"
source_empty_left_image = "Resource/Images/Background/empty_image.png"

# 动态保存修改的资源路径用dir
image_root_dir = "Database/Images"
temp_dir = "Database/Temp"
painting_image_temp_dir = temp_dir + "/temp_painting.png"
temp_left_image_dir = temp_dir + "/left_temp.png"
temp_right_image_dir = temp_dir + "/right_temp.png"
# -------------窗口-------------

win_index = None
win_painting = None
win_new_single = None
win_import_image = None
wid_preview = None
win_image_item = None
win_inspect = None

# -------------画笔-------------
pen_color_red = QColor(209, 26, 45)
pen_color_black = QColor(0, 0, 0)

pen_width = 3

# -------------画布-------------
canvas_width = 896
canvas_height = 392

# -------------数据库-------------
# 数据库路径
db_path = "Database/laps.db"
# 加载数据库驱动
db = QSqlDatabase.addDatabase("QSQLITE")
# 加载数据库文件
db.setDatabaseName(db_path)

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
image_index = None
# 当前患者的影像图片信息列表
patient_image_list = []
# 当前患者影响的修改记录
image_info_modify_record = []

inspect_lock = False

# 当前患者影像信息
def current_image():
    return patient_image_list[image_index]



# -------------用户自由设置的开关-------------
# 保存图像的模式是复制粘贴、直接剪切，True : 复制粘贴; False : 直接剪切
saveImageMode = True
# -------------口口-------------
# -------------口口-------------
