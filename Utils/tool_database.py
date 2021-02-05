# -*- coding: utf-8 -*-
# @Time : 2021/2/5 2:53 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_database.py
# @Remark : 控制数据库的工具类
# -----------------------------
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery


def singleton(cls):
    # 单下划线的作用是这个变量只能在当前模块里访问,仅仅是一种提示作用
    # 创建一个字典用来保存类的实例对象
    _instance = {}

    def _singleton(*args, **kwargs):
        # 先判断这个类有没有对象
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)  # 创建一个对象,并保存到字典当中
        # 将实例对象返回
        return _instance[cls]

    return _singleton


@singleton
class Tool_Database(object):

    def __init__(self):
        # 加载数据库驱动
        self.db = db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("../Resource/Database/laps.db")

    def open_database(self):
        return self.db.open()

    def close_database(self):
        return self.db.close()

    def create_database(self):
        pass

    def retrieve_database(self):
        pass

    def update_database(self):
        pass

    def delete_databse(self):
        pass
