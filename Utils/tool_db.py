# -*- coding: utf-8 -*-
# @Time : 2021/2/5 2:53 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_db.py
# @Remark : 控制数据库的工具类
# -----------------------------
from PyQt5.QtCore import Qt, QItemSelectionModel
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QMessageBox, QDataWidgetMapper

# 加载数据库驱动
db = QSqlDatabase.addDatabase("QSQLITE")
# 加载数据库文件
db.setDatabaseName("../Resource/Database/laps.db")


# 打开数据库
def open_db():
    if db.open():
        return True
    else:
        QMessageBox.warning("错误", "打开数据库失败")
        return False


def close_db():
    return db.close()


# 获得所有字段名称
def get_field_names(table_model):
    # 获取空记录，只留字段名
    empty_record = table_model.record()
    # 字段名与序号的字典
    field_num = {}
    for i in range(empty_record.count()):
        # 字段名
        field_name = empty_record.fieldName(i)

        # comboFields.addItem(field_name)
        field_num.setdefault(field_name)
        field_num[field_name] = i
    # 显示字典数据
    print(field_num)
    return field_num


# 打开数据表
def open_table(table_name):
    # 打开数据库
    if open_db():
        # 数据模型
        table_model = QSqlTableModel(db)
        # 设置数据表
        table_model.setTable(table_name)
        # 排序
        table_model.setSort(table_model.fieldIndex("id"), Qt.AscendingOrder)
        # 设置编辑策略;
        # OnFieldChange：字段的值变化时立即更新到数据库;
        # OnRowChange：当前行变化时更新到数据库;
        # OnManualSubmit：所有修改暂时缓存，需要手动调用submitAll()保存所有更改，或调用revertAll()函数取消所有未保存修改;
        table_model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        # 查询数据失败
        if not table_model.select():
            QMessageBox.critical("出错消息", "打开数据库表错误，出错消息\n" + table_model.lastError().text())
            return

        return table_model


def mapping(view_name, view_entity):
    if view_name == "table_patient_list":
        table_name = "patient_info"
        table_model = open_table(table_name)
        # 获取字段名和字段号
        field_num = get_field_names(table_model)
        # 设置字段显示名
        set_table_header(table_name, table_model, field_num)

        mapper = QDataWidgetMapper()
        mapper.setModel(table_model)
        mapper.setSubmitPolicy(QDataWidgetMapper.AutoSubmit)

        mapper.addMapping(view_entity, field_num[""])

        mapper.toFirst()

        selected_model = QItemSelectionModel(table_model)
        selected_model.currentChanged.connect(do_currentChanged)
        selected_model.currentRowChanged.connect(do_currentRowChanged)

        view_entity.setModel(table_model)
        view_entity.setSelectionModel(selected_model)
        view_entity.setColumnHidden(field_num[""], True)


# 设置字段显示名
def set_table_header(table_name, table_model, field_num):
    if table_name == "patient_info":
        table_model.setHeaderData(field_num["id"], Qt.Horizontal, "编号")
        table_model.setHeaderData(field_num["name"], Qt.Horizontal, "姓名")
        table_model.setHeaderData(field_num["create_date"], Qt.Horizontal, "创建日期")
        table_model.setHeaderData(field_num["modify_date"], Qt.Horizontal, "修改日期")
        table_model.setHeaderData(field_num["gender"], Qt.Horizontal, "性别")
        table_model.setHeaderData(field_num["age"], Qt.Horizontal, "年龄")
        table_model.setHeaderData(field_num["stature"], Qt.Horizontal, "身高")
        table_model.setHeaderData(field_num["weight"], Qt.Horizontal, "体重")
        table_model.setHeaderData(field_num["sbp"], Qt.Horizontal, "SBP")
        table_model.setHeaderData(field_num["dbp"], Qt.Horizontal, "DBP")
        table_model.setHeaderData(field_num["bsa"], Qt.Horizontal, "BSA")
        table_model.setHeaderData(field_num["bmi"], Qt.Horizontal, "BMI")
        table_model.setHeaderData(field_num["state"], Qt.Horizontal, "状态")

    elif table_name == "patient_image":
        table_model.setHeaderData(field_num["id"], Qt.Horizontal, "编号")
        table_model.setHeaderData(field_num["full_image"], Qt.Horizontal, "完整图片")
        table_model.setHeaderData(field_num["original_image"], Qt.Horizontal, "原始图片")
        table_model.setHeaderData(field_num["processed_image"], Qt.Horizontal, "处理图片")
        table_model.setHeaderData(field_num["left_image"], Qt.Horizontal, "左部分子图")
        table_model.setHeaderData(field_num["right_image"], Qt.Horizontal, "子图右部分")
        table_model.setHeaderData(field_num["lap"], Qt.Horizontal, "LAP")
        table_model.setHeaderData(field_num["tau"], Qt.Horizontal, "TAU")
        table_model.setHeaderData(field_num["mve"], Qt.Horizontal, "MVE")
        table_model.setHeaderData(field_num["mva"], Qt.Horizontal, "MVA")
        table_model.setHeaderData(field_num["mvs"], Qt.Horizontal, "MVS")
        table_model.setHeaderData(field_num["iase"], Qt.Horizontal, "IASE")
        table_model.setHeaderData(field_num["iasa"], Qt.Horizontal, "IASA")
        table_model.setHeaderData(field_num["iass"], Qt.Horizontal, "IASS")
        table_model.setHeaderData(field_num["state"], Qt.Horizontal, "状态")


def do_currentChanged():
    pass


def do_currentRowChanged():
    pass
