# -*- coding: utf-8 -*-
# @Time : 2021/2/5 2:53 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_db.py
# @Remark : 控制数据库的工具类
# -----------------------------
from PyQt5.QtCore import Qt, QItemSelectionModel, QDateTime
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QMessageBox, QDataWidgetMapper, QTableWidgetItem

from Utils import settings, tool_win


# 打开数据库
def open_db():
    if settings.db.open():
        tool_win.console_print("成功打开数据库！")
        return True
    else:
        QMessageBox.warning("错误", "打开数据库失败！")
        return False


# 关闭数据库
def close_db():
    tool_win.console_print("数据库关闭！")
    return settings.db.close()


def find_by_id(query_model, current):
    if not current.isValid():
        return None

    cur_record = query_model.record(current.row())

    query_model_2 = QSqlQuery(settings.db)
    query_model_2.prepare('''SELECT * FROM patient_info WHERE id = :id ORDER BY id''')

    id = cur_record.value("id")
    query_model_2.bindValue(":id", id)

    if not query_model_2.exec():
        QMessageBox.warning("错误", "数据表查询错误，出错消息\n" + query_model_2.lastError().text())
        return
    else:
        query_model_2.first()

    tool_win.console_print(query_model_2.value("name"))

    item_create_date = QTableWidgetItem(query_model_2.value("create_date"), 1000)
    item_create_date.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
    # item_name.setData(Qt.UserRole, id)
    item_id = QTableWidgetItem(str(query_model_2.value("id")), 1000)
    item_id.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

    item_name = QTableWidgetItem(str(query_model_2.value("name")), 1000)
    item_name.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

    item_gender = QTableWidgetItem(str(query_model_2.value("gender")), 1000)
    item_gender.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

    item_age = QTableWidgetItem(str(query_model_2.value("age")), 1000)
    item_age.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

    item_stature = QTableWidgetItem(str(query_model_2.value("stature")), 1000)
    item_stature.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

    item_weight = QTableWidgetItem(str(query_model_2.value("weight")), 1000)
    item_weight.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

    item_sbp = QTableWidgetItem(str(query_model_2.value("sbp")), 1000)
    item_sbp.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

    item_dbp = QTableWidgetItem(str(query_model_2.value("dbp")), 1000)
    item_dbp.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

    item_bsa = QTableWidgetItem(str(query_model_2.value("bsa")), 1000)
    item_bsa.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

    item_bmi = QTableWidgetItem(str(query_model_2.value("bmi")) + ' [' + str(query_model_2.value("bmi_degree")) + ']', 1000)
    item_bmi.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

    item_list = [item_create_date, item_id, item_name, item_gender, item_age, item_stature,
                 item_weight, item_sbp, item_dbp, item_bsa, item_bmi]

    return item_list


def find_all():
    if open_db():
        query_model = QSqlQueryModel()
        query_model.setQuery('''SELECT state, id, name FROM patient_info ORDER BY id''')
        if query_model.lastError().isValid():
            QMessageBox.warning("错误", "数据表查询错误，出错消息\n" + query_model.lastError().text())

        query_model.setHeaderData(0, Qt.Horizontal, "状态")
        query_model.setHeaderData(1, Qt.Horizontal, "编号")
        query_model.setHeaderData(2, Qt.Horizontal, "姓名")

        return query_model


# 插入项目至patient_info表
def insert_info(id, name, create_date, modify_date,
                gender, age, stature, weight, sbp, dbp, bsa, bmi, bmi_degree, state):
    tool_win.console_print("接收到的数据：")
    tool_win.console_print(id, type(id), name, type(name), create_date, type(create_date),
                           modify_date, type(modify_date), gender, type(gender),
                           age, type(age), stature, type(stature), weight, type(weight),
                           sbp, type(sbp), dbp, type(dbp), bsa, type(bsa),
                           bmi, type(bmi), bmi_degree, type(bmi_degree), state, type(state))

    query = QSqlQuery(settings.db)

    query.prepare(
        '''INSERT INTO 
            patient_info (id, name, create_date, modify_date, 
            gender, age, stature, weight, sbp, dbp, bsa, bmi, bmi_degree, state)
            VALUES
            (:id, :name, :create_date, :modify_date,
             :gender, :age, :stature, :weight, :sbp, :dbp, :bsa, :bmi, :bmi_degree, :state)'''
    )
    query.bindValue(":id", id)
    query.bindValue(":name", name)
    create_date_dt = QDateTime.fromString(create_date, "yyyy-MM-dd hh:mm:ss")
    query.bindValue(":create_data", create_date_dt)
    query.bindValue(":modify_data", modify_date)
    query.bindValue(":gender", gender)
    query.bindValue(":age", age)
    query.bindValue(":stature", stature)
    query.bindValue(":weight", weight)
    query.bindValue(":sbp", sbp)
    query.bindValue(":dbp", dbp)
    query.bindValue(":bsa", bsa)
    query.bindValue(":bmi", bmi)
    query.bindValue(":bmi_degree", bmi_degree)
    query.bindValue(":state", state)

    res = query.exec()
    if not res:
        print("错误", "插入记录错误\n" + query.lastError().text())
    else:
        print("成功！")
        # 刷新显示列表P213
        pass


# 增添项目
# def create_item():
#     open_db()
#     query = QSqlQuery(db)
#     query.exec("select * from employee where EmpNo =-1")  # 实际不查询出记录，只查询字段信息
#
#     curRec = query.record()  # 获取当前记录,实际为空记录,但有字段信息
#     curRec.setValue("EmpNo", .qryModel.rowCount() + 3000)
#
#     dlgData = QmyDialogData()
#     dlgData.setInsertRecord(curRec)  # 插入记录
#
#     ret = dlgData.exec()  # 以模态方式显示对话框
#     if (ret != QDialog.Accepted):
#         return
#
#     recData = dlgData.getRecordData()
#
#     query.prepare('''INSERT INTO employee (EmpNo,Name,Gender,Birthday,
#                 Province,Department,Salary,Memo,Photo)
#                 VALUES(:EmpNo,:Name, :Gender,:Birthday,:Province,
#                 :Department,:Salary,:Memo,:Photo)''')
#
#     query.bindValue(":EmpNo", recData.value("EmpNo"))
#     query.bindValue(":Name", recData.value("Name"))
#     query.bindValue(":Gender", recData.value("Gender"))
#     query.bindValue(":Birthday", recData.value("Birthday"))
#
#     query.bindValue(":Province", recData.value("Province"))
#     query.bindValue(":Department", recData.value("Department"))
#
#     query.bindValue(":Salary", recData.value("Salary"));
#     query.bindValue(":Memo", recData.value("Memo"));
#     query.bindValue(":Photo", recData.value("Photo"));
#
#     res = query.exec()  # 执行SQL语句
#     if (res == False):
#         QMessageBox.critical(, "错误",
#                              "插入记录错误\n" + query.lastError().text())
#     else:  # 插入，删除记录后需要重新设置SQL语句查询
#         sqlStr = .qryModel.query().executedQuery()  # 执行过的SELECT语句
#         .qryModel.setQuery(sqlStr)  # reset 重新查询数据
#
#
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
        table_model = QSqlTableModel(settings.db)
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
