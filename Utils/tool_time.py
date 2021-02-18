# -*- coding: utf-8 -*-
# @Time : 2021/2/5 9:08 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_time.py
# @Remark : 控制时间的工具类
# -----------------------------
import datetime

from PyQt5.QtCore import QTime, QDate, QDateTime


def q_date_current_date():
    result = QDate.currentDate()
    # tool_win.logging(result)
    return result


def q_time_current_time():
    result = QTime.currentTime()
    # tool_win.logging(result)
    return result


def q_datetime_current_datetime():
    result = QDateTime.currentDateTime()
    # tool_win.logging(result)
    return result


def current_date():
    result = datetime.datetime.now().strftime('%Y/%m/%d')
    # tool_win.logging(result)
    return result


def current_time_without_second():
    result = datetime.datetime.now().strftime('%H:%M')
    # tool_win.logging(result)
    return result


def current_time_with_second():
    result = datetime.datetime.now().strftime('%H:%M:%S')
    # tool_win.logging(result)
    return result


def current_datetime():
    result = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    # tool_win.logging(result)
    return result


if __name__ == "__main__":
    current_date()
    current_time_with_second()
    current_time_without_second()
    current_datetime()
