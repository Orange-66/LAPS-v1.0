# -*- coding: utf-8 -*-
# @Time : 2021/1/24 4:15 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS
# @File : tool_win.py
# @Remark : 控制日志的工具类
# -----------------------------
import logging

# -------------日志-------------
log = logging
log.basicConfig(level=logging.DEBUG,
                format='%(asctime)s - %(levelname)s - %(message)s',
                filename='Docs/logging.txt',
                filemode='w')
# 日志记录开关
log.disable(log.INFO)
log.disable(log.WARNING)
log.disable(log.DEBUG)
# 打印开关
is_console = True


# 成功操作
def success(*args):
    result_str = to_string(*args)
    console(result_str)
    log.info(result_str)


# 失败操作
def failure(*args):
    result_str = to_string(*args)
    console(result_str)
    log.warning(result_str)


# 测试操作
def debug(*args):
    result_str = to_string(*args)
    console(result_str)
    log.debug(result_str)


# 在控制条打印消息
def console(console_str):
    if is_console:
        print(console_str)


# 将输入的参数转为一整个字符串
def to_string(*args):
    result_str = ''
    for i in args:
        result_str += str(i)

    return result_str
