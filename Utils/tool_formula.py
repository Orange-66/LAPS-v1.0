# -*- coding: utf-8 -*-
# @Time : 2021/2/5 10:31 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_formula.py
# @Remark : 控制公式的工具类
# -----------------------------

# bmi公式
from Utils import tool_log


def formula_bmi(stature, weight):
    tool_log.debug("1231231212312", stature, weight)
    tool_log.debug(weight / (stature/100) ** 2)
    return weight / (stature/100) ** 2


# bsa公式
def formula_bsa(stature, weight):
    # tool_log.debug(stature * 0.0061 + weight * 0.0128 - 0.1529)
    return stature * 0.0061 + weight * 0.0128 - 0.1529


def formula_bmi_degree(bmi):
    # tool_log.debug(bmi)
    if bmi < 18.5:
        return "偏瘦"
    elif 18.5 <= bmi < 25.0:
        return "正常"
    elif 25.0 <= bmi < 30.0:
        return "偏胖"
    elif 30.0 <= bmi < 35.0:
        return "肥胖"
    elif 35.0 <= bmi < 40.0:
        return "重度肥胖"
    else:
        return "极重度肥胖"


# 保留N位小数
def set_round(num, place):
    return round(num, place)

