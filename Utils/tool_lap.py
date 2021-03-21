# -*- coding: utf-8 -*-
# @Time : 2021/3/11 10:52 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_lap.py
# @Remark : 左房压计算工具
# -----------------------------
from Utils import tool_log
from Utils.model_lap import function


# 处理原始图片
def process_original_image(original_image_path):
    """

    Args:
        original_image_path: String, 图片路径

    Returns:
        返回lap数据以及process_image_path
    """
    tool_log.debug("process_original_image",original_image_path)

    lap, process_image_path = function.process_original_image(original_image_path)
    return lap, process_image_path
