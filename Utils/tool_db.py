# -*- coding: utf-8 -*-
# @Time : 2021/2/5 2:53 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_db.py
# @Remark : 控制数据库的工具类
# -----------------------------
from PyQt5.QtCore import Qt, QDateTime, QFile, QIODevice
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlQueryModel, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from Utils import settings, tool_log


# 打开数据库-完成
def open_db():
    # 如果settings类中的db可以打开
    if settings.db.open():
        # 则在日志中记录数据库打开成功
        tool_log.debug("tool_db - open_db, 成功打开数据库！")
        return True
    else:
        # 如果不可以打开
        # 则在日志中记录数据库打开失败
        tool_log.debug("tool_db - open_db, 打开数据库失败！")
        # 同时予以用户以提示
        QMessageBox.warning(settings.win_index, "错误", "打开数据库失败！")
        return False


# 关闭数据库-完成
def close_db():
    # 在日志中记录数据库的关闭
    tool_log.debug("tool_db - close_db, 数据库关闭！")
    # 关闭数据库
    return settings.db.close()


# 打开数据表 - 未被使用？？？
def open_table(table_name, order_by="patient_id", order_type=Qt.AscendingOrder):
    # 打开数据库
    if open_db():
        # 数据模型
        table_model = QSqlTableModel(settings.db)
        # 设置数据表
        table_model.setTable(table_name)
        # 排序
        table_model.setSort(table_model.fieldIndex(order_by), order_type)
        # 设置编辑策略;
        # OnFieldChange：字段的值变化时立即更新到数据库;
        # OnRowChange：当前行变化时更新到数据库;
        # OnManualSubmit：所有修改暂时缓存，需要手动调用submitAll()保存所有更改，或调用revertAll()函数取消所有未保存修改;
        table_model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        # 查询数据失败
        if not table_model.select():
            QMessageBox.critical(settings.win_index, "错误", "打开数据库表错误，出错消息\n" + table_model.lastError().text())
            return

        return table_model


# 在info表中依据病人id查找项目-完成
def find_info_by_patient_id(query_model, row):
    """

    Args:
        query_model: QSqlQueryModel
        row: Int

    Returns:
        找到的患者的所有信息
    """
    # 获取该行记录
    cur_record = query_model.record(row)
    # 设置查询条件：以病人id为搜索条件，按照修改时间进行排序
    query_model_2 = QSqlQuery(settings.db)
    query_model_2.prepare('''SELECT * FROM patient_info 
                            WHERE patient_id = :patient_id''')
    # 获得记录中patient_id属性的值，并赋值给sql语句
    patient_id = cur_record.value("patient_id")
    query_model_2.bindValue(":patient_id", patient_id)

    # 执行sql语句
    if not query_model_2.exec():
        # 如果执行失败，提示用户执行失败，并将相应的情况记录在日志中
        QMessageBox.warning("错误", "数据表查询错误，出错消息\n" + query_model_2.lastError().text())
        tool_log.debug("tool_db - find_in_info_by_patient_id, 数据表查询错误，出错消息", query_model_2.lastError().text())
        return None

    # 获取查询到的第一个项目
    query_model_2.first()

    tool_log.debug("tool_db - find_in_info_by_patient_id, 患者姓名：", query_model_2.value("name"),
                   "患者id：", query_model_2.value("patient_id"))

    # 将获取到的第一个项目中的每一个属性建造成一个QTableWidgetItem对象，最后一并放入item_list中
    item_create_date = query_model_2.value("create_date")
    item_id = query_model_2.value("patient_id")
    item_name = query_model_2.value("name")
    item_gender = query_model_2.value("gender")
    item_age = query_model_2.value("age")
    item_stature = query_model_2.value("stature")
    item_weight = query_model_2.value("weight")
    item_sbp = query_model_2.value("sbp")
    item_dbp = query_model_2.value("dbp")
    item_bsa = query_model_2.value("bsa")
    item_bmi = str(query_model_2.value("bmi")) + " [" + str(query_model_2.value("bmi_degree")) + "]"

    item_list = {"create_date": item_create_date, "patient_id": item_id, "name": item_name,
                 "gender": item_gender, "age": item_age, "stature": item_stature,
                 "weight": item_weight, "sbp": item_sbp, "dbp": item_dbp,
                 "bsa": item_bsa, "bmi": item_bmi}

    return item_list


# 依据关键字查询所有项目-完成
def find_info_by_keyword(keyword=""):
    """

    Args:
        keyword: String

    Returns:
        返回根据keyword找到的所有的患者信息
    """
    if open_db():
        query_model = QSqlQueryModel()
        # 如果keyword为空，则除查询数据库中全部数据的前100项数据
        if keyword == "":
            query_model.setQuery('''SELECT state, patient_id, name 
                                    FROM patient_info 
                                    ORDER BY modify_date
                                    LIMIT 100''')
        else:
            query = QSqlQuery(settings.db)
            query.prepare('''SELECT state, patient_id, name 
                                    FROM patient_info 
                                    WHERE name=:keyword OR patient_id=:keyword
                                    ORDER BY modify_date DESC 
                                    LIMIT 100''')

            query.bindValue(":keyword", keyword)
            if not query.exec():
                # 如果执行失败，提示用户执行失败，并将相应的情况记录在日志中
                QMessageBox.warning(settings.win_index, "错误", "数据表查询错误，出错消息\n" + query.lastError().text())
                tool_log.debug("find_by_keyword, 数据表查询错误，出错消息", query.lastError().text())
                return None

            query_model.setQuery(query)

        if query_model.lastError().isValid():
            # 如果执行失败，提示用户执行失败，并将相应的情况记录在日志中
            QMessageBox.warning(settings.win_index, "错误", "数据表查询错误，出错消息\n" + query_model.lastError().text())
            tool_log.debug("find_by_keyword", "数据表查询错误，出错消息", query_model.lastError().text())

        query_model.setHeaderData(0, Qt.Horizontal, "状态")
        query_model.setHeaderData(1, Qt.Horizontal, "编号")
        query_model.setHeaderData(2, Qt.Horizontal, "姓名")

        return query_model


# 插入项目至patient_info表-完成
def insert_info(patient_id, name, create_date, modify_date,
                gender, age, stature, weight, sbp, dbp, bsa, bmi, bmi_degree, state):
    tool_log.debug("tool_db - insert_into_info, 接收到的数据：", patient_id, type(patient_id), name, type(name), create_date,
                   type(create_date),
                   modify_date, type(modify_date), gender, type(gender),
                   age, type(age), stature, type(stature), weight, type(weight),
                   sbp, type(sbp), dbp, type(dbp), bsa, type(bsa),
                   bmi, type(bmi), bmi_degree, type(bmi_degree), state, type(state))

    query = QSqlQuery(settings.db)

    query.prepare(
        '''INSERT INTO 
            patient_info (patient_id, name, create_date, modify_date, 
            gender, age, stature, weight, sbp, dbp, bsa, bmi, bmi_degree, state)
            VALUES
            (:patient_id, :name, :create_date, :modify_date,
             :gender, :age, :stature, :weight, :sbp, :dbp, :bsa, :bmi, :bmi_degree, :state)'''
    )
    query.bindValue(":patient_id", patient_id)
    query.bindValue(":name", name)
    query.bindValue(":create_date", create_date)
    # 没有写错，初次插入的时候，修改日期即创建日期
    query.bindValue(":modify_date", create_date)
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
        tool_log.debug("tool_db - insert_info, 错误", "插入记录错误\n" + query.lastError().text())
        QMessageBox.warning(settings.win_index, "错误", "数据库插入记录错误，出错消息\n" + query.lastError().text())
    else:
        tool_log.debug("tool_db - insert_info, 成功！")
        # 刷新列表
        settings.win_index.refresh_window()


# 根据患者id查询image表
def find_image_by_patient_id(query_model, row):
    cur_record = query_model.record(row)

    query_model_2 = QSqlQuery(settings.db)
    query_model_2.prepare('''SELECT * FROM patient_image WHERE patient_id = :patient_id''')

    patient_id = cur_record.value("patient_id")
    query_model_2.bindValue(":patient_id", patient_id)

    if not query_model_2.exec():
        QMessageBox.warning(settings.win_index, "错误", "数据表查询错误，出错消息\n" + query_model_2.lastError().text())
        tool_log.debug("find_image_by_patient_id, 数据表查询错误，出错消息" + query_model_2.lastError().text())
        return False

    patient_image_list = []

    while query_model_2.next():
        uncropped_image_path = query_model_2.value("uncropped_image_path")
        uncropped_image = QPixmap(uncropped_image_path)

        original_image_path = query_model_2.value("original_image_path")
        original_image = QPixmap(original_image_path)

        processed_image_path = query_model_2.value("processed_image_path")
        processed_image = QPixmap(processed_image_path)

        item_id = str(query_model_2.value("image_id"))
        item_lap = str(query_model_2.value("lap"))
        item_tau = str(query_model_2.value("tau"))
        item_mve = str(query_model_2.value("mve"))
        item_mva = str(query_model_2.value("mva"))
        item_mvs = str(query_model_2.value("mvs"))
        item_iase = str(query_model_2.value("iase"))
        item_iasa = str(query_model_2.value("iasa"))
        item_iass = str(query_model_2.value("iass"))

        image_item = {'id': item_id, 'lap': item_lap, 'tau': item_tau,
                      'uncropped_image': uncropped_image, 'uncropped_image_path': uncropped_image_path,
                      'original_image': original_image, 'original_image_path': original_image_path,
                      'processed_image': processed_image, 'processed_image_path': processed_image_path,
                      'mve': item_mve, 'mva': item_mva, 'mvs': item_mvs,
                      'iase': item_iase, 'iasa': item_iasa, 'iass': item_iass}

        patient_image_list.append(image_item)

    settings.image_index = 0
    settings.patient_image_list = patient_image_list

    return len(settings.patient_image_list)


# 将字典中的str类型数据转换成QTableWidgetItem类型
def dic_to_table_widget_item_list(dictionary):
    widget_item_list = {}
    for key, value in dictionary.items():
        item = QTableWidgetItem(str(value), 1000)
        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        widget_item_list[key] = item

    return widget_item_list


# 插入图片-完成
def insert_image(patient_id, uncropped_image_path):
    """

    Args:
        patient_id: Int
        uncropped_image_path: String

    Returns:

    """
    tool_log.debug("tool_db - insert_image, 接收到的数据：", patient_id, type(patient_id),
                   uncropped_image_path, type(uncropped_image_path))

    query = QSqlQuery(settings.db)

    query.prepare(
        '''INSERT INTO 
            patient_image (patient_id, uncropped_image_path, original_image_path)
            VALUES
            (:patient_id, :uncropped_image_path, :original_image_path)'''
    )
    query.bindValue(":patient_id", patient_id)
    query.bindValue(":uncropped_image_path", uncropped_image_path)
    query.bindValue(":original_image_path", uncropped_image_path)

    res = query.exec()
    if not res:
        QMessageBox.warning(settings.win_index, "错误", "插入记录错误," + query.lastError().text())
        tool_log.debug("insert_image，错误 - 插入记录错误" + query.lastError().text())
    else:
        tool_log.debug("insert_image，成功！")
        # 刷新显示列表
        settings.win_index.refresh_window()


# 修改患者processed_image信息
def update_processed_image(image_id, processed_image):
    pass


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
    tool_log.debug("get_field_names, field_num", field_num)
    return field_num


# 设置字段显示名
def set_table_header(table_name, table_model, field_num):
    if table_name == "patient_info":
        table_model.setHeaderData(field_num["patient_id"], Qt.Horizontal, "编号")
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
        table_model.setHeaderData(field_num["patient_id"], Qt.Horizontal, "编号")
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


# 删除患者信息
def delete_patient(patient_id):
    tool_log.debug("delete_patient，patient_id：", patient_id)

    # 删除patient_image列表中的项目
    query_image = QSqlQuery(settings.db)

    query_image.prepare(
        '''DELETE FROM patient_image 
            WHERE patient_id = :patient_id'''
    )
    query_image.bindValue(":patient_id", patient_id)

    image_res = query_image.exec()
    if not image_res:
        tool_log.debug("insert_image，错误", "删除记录失败\n" + query_image.lastError().text())
        return

    # 删除patient_info列表中的项目
    query_patient = QSqlQuery(settings.db)

    query_patient.prepare(
        '''DELETE FROM patient_info
            WHERE patient_id = :patient_id'''
    )
    query_patient.bindValue(":patient_id", patient_id)

    patient_res = query_patient.exec()

    if not patient_res:
        tool_log.debug("insert_image，错误", "删除记录失败\n" + patient_res.lastError().text())
    else:
        tool_log.debug("insert_image，删除记录成功！")


# 删除图片信息
def delete_current_image(image_id):
    tool_log.debug("delete_current_image，image_id：", image_id)

    # 删除patient_image列表中的项目
    query_image = QSqlQuery(settings.db)

    query_image.prepare(
        '''DELETE FROM patient_image 
            WHERE image_id = :image_id'''
    )
    query_image.bindValue(":image_id", image_id)

    image_res = query_image.exec()
    if not image_res:
        tool_log.debug("insert_image，错误", "删除记录失败" + query_image.lastError().text())
        QMessageBox.warning(settings.win_index, "错误", "删除记录失败")
    else:
        tool_log.debug("insert_image，成功", "成功删除记录" + query_image.lastError().text())
        QMessageBox.about(settings.win_index, "成功", "成功删除记录")

    settings.win_image_item.close()
