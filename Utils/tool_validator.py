#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/3/30 16:26
# @Author : Qi Tian yue
# @Github : Orange-66
# @Project : LAPS
# @File : tool_validator.py
# @Remark : 合法性检测工具类
# -----------------------------
import re

from Utils import tool_log


# 新增患者信息
def new_single(patient_id, name, gender, age,
               stature, weight, sbp, dbp):
    tool_log.debug('new_single', patient_id, name, gender, age,
                   stature, weight, sbp, dbp)
    result = True
    reason = '\n'
    if not len(str(patient_id)):
        result = False
        reason += '请填写患者编号；\n'

    if not len(str(name)):
        result = False
        reason += '请填写患者姓名；\n'

    if not len(str(gender)):
        result = False
        reason += '请选择患者性别；\n'

    if age == 0:
        result = False
        reason += '请填写患者年龄；\n'

    if stature == 0:
        result = False
        reason += '请填写患者身高；\n'

    if weight == 0:
        result = False
        reason += '请填写患者体重；\n'

    if sbp == 0:
        result = False
        reason += '请填写收缩压SBP；\n'

    if dbp == 0:
        result = False
        reason += '请填写舒张压DBP；\n'

    return result, reason


# 判断当前患者影像列表的状态（是否都已经查看核实）
def patient_image_state(image_list):
    for image in image_list:
        if type(image['processed_image_path']) != str or image['processed_image_path'] == '':
            return False

    return True


# 判断当前修改的患者图像信息数值是否合理
def table_image_info(text):
    if re.fullmatch("\d+(\.\d+)?", text):
        return True
    else:
        return False