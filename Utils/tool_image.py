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


# 剪裁图片
def crop_image(image, lt, rt, lb, rb):
    return image.crop((lt, rt, lb, rb))