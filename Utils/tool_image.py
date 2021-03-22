# -*- coding: utf-8 -*-
# @Time : 2021/2/20 4:15 上午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_image.py
# @Remark : 图片处理工具类
# -----------------------------
from PyQt5.QtCore import Qt
# 剪裁图片
from PyQt5.QtGui import QPixmap
from PIL import Image
from Utils import tool_trans, settings, tool_file


# 设置图片大小
def set_image(image, window):
    if image.height() > 600 or image.width() > 900:
        scaled_image = image.scaled(900, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        window.setFixedSize(scaled_image.width(), scaled_image.height())
        window.resize(scaled_image.size())
        window.label.resize(scaled_image.size())
        return scaled_image
    else:
        window.setFixedSize(image.width(), image.height())
        window.resize(image.size())
        window.label.resize(image.size())
        return image


# 将image填充至label中
def set_image_by_label(image, label, width=900, height=600):
    if isinstance(image, str):
        scaled_image = QPixmap(image).scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(scaled_image)
    else:
        scaled_image = image.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(scaled_image)


# 将pixmap格式的图片转换成pil类型的图片
def pixmap_to_pil(pixmap_image):
    q_image = tool_trans.pixmap_to_QImage(pixmap_image)
    return tool_trans.QImage_to_Image(q_image)


# 将pil格式的图片转换成pixmap类型的图片
def pil_to_pixmap(pil_image):
    q_image = tool_trans.Image_to_QImage(pil_image)
    return tool_trans.QImage_to_pixmap(q_image)


# 读取图片
def open_image(image_path):
    return Image.open(image_path)


# 剪裁图片
def crop_image_by_path(image_path, x1, y1, x2, y2):
    image = open_image(image_path)
    cropped_image = image.crop((x1, y1, x2, y2))
    return cropped_image


# 剪裁图片
def crop_image(image, x1, y1, x2, y2):
    cropped_image = image.crop((x1, y1, x2, y2))
    return cropped_image

# 粘贴图片
def paste_image(original_image_path, target_image_path, x, y):
    original_image = open_image(original_image_path)
    target_image = open_image(target_image_path)

    target_image.paste(original_image, (x, y))
    return target_image


# 保存图片
def save_image(image_path, dst_path):
    if settings.saveImageMode:
        tool_file.copy_file(image_path, dst_path)
    else:
        tool_file.move_file(image_path, dst_path)

# 保存图片到指定路径
def save_image_to_dir(image, save_path):
    if image:
        tool_file.make_dir(save_path)
        image.save(save_path)