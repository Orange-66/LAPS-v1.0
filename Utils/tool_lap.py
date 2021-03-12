# -*- coding: utf-8 -*-
# @Time : 2021/3/11 10:52 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_lap.py
# @Remark : 左房压计算工具
# -----------------------------
from Utils import tool_win
from Utils.model_lap import function


# 处理原始图片
def process_original_image(original_image):
    tool_win.logging("process_original_image",original_image)

    lap, process_image = function.process_original_image(original_image)
    return lap, process_image
