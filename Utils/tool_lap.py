# -*- coding: utf-8 -*-
# @Time : 2021/3/11 10:52 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_lap.py
# @Remark : 左房压计算工具
# -----------------------------
from Utils import tool_log, tool_image, tool_formula
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

    lap, tau, process_image_path = function.process_original_image(original_image_path)
    # 修正输出的图片
    cropped_image = tool_image.crop_image_by_path(process_image_path, 82, 136, 574, 350)
    tool_image.save_image_to_dir(cropped_image, process_image_path)
    lap = tool_formula.set_round(lap, 4)
    tau = tool_formula.set_round(tau, 4)
    # 设置lap返回的精确度
    return lap, tau, process_image_path
