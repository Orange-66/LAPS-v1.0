# -*- coding: utf-8 -*-
# @Time : 2021/2/20 4:15 上午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_image.py
# @Remark : 
# -----------------------------
from PIL import Image
import os
from PyQt5.QtCore import Qt
# 剪裁图片
from PyQt5.QtGui import QPixmap


def crop_image(image, lt, rt, lb, rb):
    return image.crop((lt, rt, lb, rb))


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
def set_image_by_label(image, label):
    print("12312312312", type(image))
    if isinstance(image, str):
        scaled_image = QPixmap(image).scaled(900, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(scaled_image)
    else:
        scaled_image = image.scaled(900, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(scaled_image)
