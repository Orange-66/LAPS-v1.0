# -*- coding: utf-8 -*-
# @Time : 2021/1/22 5:01 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : win_index.py
# @Remark : 主窗口
# -----------------------------
from PyQt5.QtCore import pyqtSlot, Qt, QItemSelectionModel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAbstractItemView, QMessageBox, QTableWidgetItem)
from PyQt5 import QtCore

from PyUI.ui_index import Ui_Index
from Utils import settings, tool_win, tool_db, tool_image, tool_lap, tool_log, tool_file
from Widget.wid_preview import Wid_Preview
from Window.win_image_item import Win_Image_Item
from Window.win_inspect import Win_Inspect
from Window.win_painting import Win_Painting
from Window.win_new_single import Win_New_Single
from Window.win_import_image import Win_Import_Image

class Win_Index(QMainWindow):
    # False 代表图像信息的监听关闭
    image_info_lock = False

    # ========================构造函数========================
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.__ui = Ui_Index()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面

        # table_patient_list的显示属性设置
        self.__ui.table_patient_list.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.__ui.table_patient_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.__ui.table_patient_list.setAlternatingRowColors(True)
        self.__ui.table_patient_list.verticalHeader().hide()
        self.__ui.table_patient_list.verticalHeader().setDefaultSectionSize(22)
        self.__ui.table_patient_list.horizontalHeader().setDefaultSectionSize(53)

        # 日期与标题的单元格合并
        self.__ui.table_image_info.setSpan(0, 0, 1, 4)
        self.__ui.table_image_info.setSpan(1, 1, 1, 3)

        # 设置表头
        item_title = QTableWidgetItem("患者基本信息", 1000)
        item_title.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        item_title.setFlags(QtCore.Qt.NoItemFlags)
        self.__ui.table_image_info.setItem(0, 0, item_title)

        # 刷新界面
        self.refresh_window()
        self.image_info_lock = True

        settings.wid_preview = Wid_Preview()

    # ========================重载事件函数========================
    def closeEvent(self, event):
        tool_win.close_all()
        tool_db.close_db()

    # ========================自动关联槽函数========================
    @pyqtSlot(bool)
    # 新建按钮-点击-槽函数
    def on_act_new_single_triggered(self):
        tool_log.debug("on_btn_new_single_clicked")
        settings.win_new_single = Win_New_Single()
        settings.win_new_single.show()

    @pyqtSlot(bool)
    # 导入按钮-点击-槽函数
    def on_act_import_triggered(self):
        self.image_info_lock = False
        tool_log.debug("on_btn_import_clicked")
        settings.win_import_image = Win_Import_Image()
        settings.win_import_image.show()
        self.image_info_lock = True

    @pyqtSlot(bool)
    # 绘画按钮-点击-槽函数
    def on_act_painting_triggered(self):
        tool_log.debug("on_btn_painting_clicked")
        settings.win_painting = Win_Painting()
        settings.win_painting.show()

    @pyqtSlot(bool)
    # 预测按钮-点击-槽函数
    def on_act_predict_triggered(self):
        tool_log.debug("on_act_predict_triggered")
        self.image_info_lock = False
        self.set_processed_image(None)
        self.image_info_lock = True

    @pyqtSlot(bool)
    # 撤销按钮-点击-槽函数-未完成
    def on_act_backward_triggered(self):
        tool_log.debug("on_act_backward_triggered")
        if len(settings.image_info_modify_record):
            self.image_info_lock = False
            deleted_item = settings.image_info_modify_record.pop()
            self.__set_item_text(deleted_item['row'], deleted_item['column'], deleted_item['before'])
            self.image_info_lock = True

    @pyqtSlot(bool)
    # 取消按钮-点击-槽函数-未完成
    def on_act_cancel_triggered(self):
        tool_log.debug("on_act_cancel_triggered")

        self.image_info_lock = False
        item_list = tool_db.dic_to_table_widget_item_list(settings.current_image())
        self.__refresh_mv_ias(item_list)
        settings.image_info_modify_record.clear()
        self.image_info_lock = True

    @pyqtSlot(bool)
    # 删除按钮-点击-槽函数
    def on_act_delete_triggered(self):
        tool_log.debug("on_act_delete_triggered - 删除patient_id", settings.current_patient_id)

        if QMessageBox.warning(settings.win_index, "注意", "确认删除此患者数据？", QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.Yes) == QMessageBox.Yes:
            tool_db.delete_patient(settings.current_patient_id)
            file_dir = tool_file.make_path(settings.image_root_dir,
                                           settings.current_patient_id + '-' + settings.current_patient_name)
            delete_mode = 'e'
            tool_file.delete_file(file_dir, delete_mode)
            # 刷新显示列表
            settings.win_index.refresh_window()
            settings.image_info_modify_record.clear()

    @pyqtSlot()
    # 保存按钮-点击-槽函数-未完成
    def on_act_save_triggered(self):
        tool_log.debug("on_act_save_triggered")
        self.image_info_lock = False
        mv_ias_list = self.__get_mv_ias_list()
        tool_db.update_mv_ias(settings.patient_image_list[settings.image_index]['image_id'], mv_ias_list)
        settings.image_info_modify_record.clear()
        self.image_info_lock = True

    @pyqtSlot()
    # 快速查看按钮-点击-槽函数
    def on_act_inspect_triggered(self):
        tool_log.debug("on_act_inspect_triggered")
        self.image_info_lock = False
        settings.win_inspect = Win_Inspect()
        settings.win_inspect.show()

    @pyqtSlot()
    # 上一张图片按钮-点击-槽函数
    def on_btn_up_page_clicked(self):
        tool_log.debug("on_btn_up_page_clicked")
        if settings.image_index > 0:
            self.__update_mv_ias(settings.current_image())
            settings.image_index -= 1
            current_image_info = settings.patient_image_list[settings.image_index]
            self.__refresh_image_info(current_image_info)

    @pyqtSlot()
    # 下一张图片按钮-点击-槽函数
    def on_btn_down_page_clicked(self):
        tool_log.debug("on_btn_down_page_clicked")
        if settings.image_index + 1 < len(settings.patient_image_list):
            self.__update_mv_ias(settings.current_image())
            settings.image_index += 1
            current_image_info = settings.patient_image_list[settings.image_index]
            self.__refresh_image_info(current_image_info)

    @pyqtSlot()
    # 图片信息按钮-点击-槽函数
    def on_btn_page_info_clicked(self):
        tool_log.debug("on_btn_page_info_clicked")
        if len(settings.patient_image_list):
            settings.win_image_item = Win_Image_Item()
            settings.win_image_item.show()
        else:
            QMessageBox.about(settings.win_index, "提示", "当前情况下没有图片可看！")

    @pyqtSlot()
    # 搜索框-回车-槽函数
    def on_line_search_bar_returnPressed(self):
        tool_log.debug("on_line_search_bar_returnPressed", self.__ui.line_search_bar.text())
        keyword = self.__ui.line_search_bar.text()
        self.refresh_window(keyword)

    @pyqtSlot(QTableWidgetItem)
    # 图像信息记录-改变-槽函数
    def on_table_image_info_itemChanged(self, item):
        if self.image_info_lock:
            tool_log.debug("on_table_image_info_itemChanged", item.text(), item.column(), item.row())

            flag = None
            for i in settings.image_info_modify_record:
                if i['type'] == item.data(Qt.UserRole):
                    flag = i

            if flag:
                settings.image_info_modify_record.append(
                    {'after': item.text(),
                     'before': flag['after'],
                     'type': item.data(Qt.UserRole),
                     'column': item.column(),
                     'row': item.row()}
                )
            else:
                print(item.text(), item.data(Qt.UserRole), item.column(), item.row())
                settings.image_info_modify_record.append(
                    {'after':item.text(),
                     'before': settings.patient_image_list[settings.image_index][item.data(Qt.UserRole)],
                     'type': item.data(Qt.UserRole),
                     'column':item.column(),
                     'row':item.row()})

            tool_log.debug("on_table_image_info_itemChanged", settings.image_info_modify_record)



    # ========================自定义函数========================
    # 刷新界面
    def refresh_window(self, keyword=''):
        tool_log.debug("refresh_window, 界面刷新！")
        self.__refresh_patient_list(keyword)
        self.refresh_image_list()

    # 刷新患者列表
    def __refresh_patient_list(self, keyword=''):
        self.image_info_lock = False
        # 查询并刷新患者列表
        self.query_model = tool_db.find_info_by_keyword(keyword)
        select_model = QItemSelectionModel(self.query_model)
        select_model.currentRowChanged.connect(self.do_currentRowChanged)

        self.__ui.table_patient_list.setModel(self.query_model)
        self.__ui.table_patient_list.setSelectionModel(select_model)

        class Current:
            def isValid(self):
                return True

            def row(self):
                return 0

        self.do_currentRowChanged(Current())
        self.image_info_lock = True

    # 刷新相册列表
    def refresh_image_list(self, row=0):
        if settings.image_index and len(settings.patient_image_list):
            self.__update_mv_ias(settings.current_image())
        if settings.inspect_lock:
            current_image_info = settings.patient_image_list[0]
            tool_log.debug("refresh_image_list", current_image_info)
            self.__refresh_image_info(current_image_info)
        else:
            if tool_db.find_image_by_patient_id(self.query_model, row):
                current_image_info = settings.patient_image_list[0]
                tool_log.debug("refresh_image_list", current_image_info)
                self.__refresh_image_info(current_image_info)
            else:
                tool_log.debug("refresh_image_list", "None")
                self.__refresh_image_info(None)

    # 判断是否更新mv与ias
    def __update_mv_ias(self, previous_image_info):
        if len(settings.image_info_modify_record):
            result = QMessageBox.information(self, '提示', '是否对已修改的数据进行保存？', QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.Yes)
            if result == QMessageBox.Yes:
                mv_ias_list = self.__get_mv_ias_list()
                for key, value in mv_ias_list.items():
                    settings.current_image()[key] = value
                tool_db.update_mv_ias(previous_image_info['image_id'], mv_ias_list)
    
            settings.image_info_modify_record.clear()
            
    # 更新图像信息
    def __refresh_image_info(self, current_image_info):
        self.image_info_lock = False
        if current_image_info:
        # 刷新btn_down_page按钮上文字
            current_processed_image = current_image_info['processed_image']
            current_original_image = current_image_info['original_image']
            uncropped_image_path = current_image_info['uncropped_image_path']
        else:
            current_processed_image = None
            current_original_image = None
            uncropped_image_path = None

        self.__set_others_image(uncropped_image_path)
        self.__refresh_btn_page_info()
        self.__set_original_image(current_original_image)

        self.set_processed_image(current_processed_image)

        self.image_info_lock = True

    # 用户点击患者列表中的Item所出发的刷新界面函数
    def do_currentRowChanged(self, current, previous=""):
        # 当前所选择的是否合理
        if current.isValid():
            # 获取选择的患者的所有信息，根据其id
            item_list = tool_db.find_info_by_patient_id(self.query_model, current.row())
            # 如果得到的数据是有效的，则刷新患者信息列表
            if item_list:
                self.__refresh_info_patient(tool_db.dic_to_table_widget_item_list(item_list))

                # 更新当前画着的id以及姓名
                settings.current_patient_id = self.query_model.record(current.row()).value("patient_id")
                settings.current_patient_name = self.query_model.record(current.row()).value("name")

                # 刷新患者影响列表
                self.refresh_image_list(current.row())

    # 设置原始图片
    def __set_original_image(self, current_original_image):
        # 如果图象是无效的则将图片为空的图像素材打在相应界面上
        if not current_original_image:
            tool_image.set_image_by_label(settings.source_empty_image, self.__ui.label_original_image)
        # 反之提供相应的图片
        else:
            tool_image.set_image_by_label(current_original_image, self.__ui.label_original_image)

    # 设置处理后的图片
    def set_processed_image(self, current_processed_image):
        # tool_log.debug("set_processed_image", current_processed_image)
        # 如果当前还没有计算过相应的图片的lap,则为原图计算lap并同时产生相应的处理后的processed_image
        if not len(settings.patient_image_list):
            tool_image.set_image_by_label(settings.source_empty_image, self.__ui.label_processed_image)
            return

        processed_image_info = settings.patient_image_list[settings.image_index]
        if current_processed_image:
            # tool_log.debug("set_processed_image", settings.patient_image_list, settings.image_index)

            # 刷新图片信息板
            self.__refresh_info_image(tool_db.dic_to_table_widget_item_list(processed_image_info))

            tool_image.set_image_by_label(current_processed_image, self.__ui.label_processed_image)
            # processed_image_info['processed_image'] = current_processed_image
        # 设置处理后的图片到相应的图片位置上
        else:

            # 处理并计算得出lap以及相应的图片
            print("processed_image_info['uncropped_image_path']",processed_image_info['uncropped_image_path'])
            lap, tau, processed_image_path = \
                tool_lap.process_original_image(
                    processed_image_info['uncropped_image_path'])

            if settings.inspect_lock:
                # LAP
                # 保存在当前list中
                processed_image_info['lap'] = str(lap)

                # TAU
                # 保存在当前list中
                processed_image_info['tau'] = str(tau)

                processed_image_info['processed_image_path'] = processed_image_path
                processed_image_info['processed_image'] = QPixmap(processed_image_path)
            else:
                patient_id = str(settings.current_patient_id)
                patient_name = settings.current_patient_name
                image_id = processed_image_info['image_id']

                # 保存processed图片的路径以及文件名
                new_processed_name = tool_file.make_filename()

                # 旧文件的文件名
                old_processed_name = tool_file.get_filename(processed_image_path)
                # 重命名后的文件名
                processed_filename = tool_file.rename_file(old_processed_name, new_processed_name)
                # 保存processed文件的路径名
                processed_save_path = tool_file.make_path(settings.image_root_dir,
                                                          patient_id + "-" + patient_name, "processed")
                # processed—image保存路径并保存到相应路径上
                new_processed_image_path = tool_file.make_path(processed_save_path, processed_filename)
                tool_image.save_image(processed_image_path, new_processed_image_path)

                # 将得到的图片存储到数据库中
                tool_db.update_image(image_id, new_processed_image_path)

                processed_image_info['processed_image_path'] = new_processed_image_path
                processed_image_info['processed_image'] = QPixmap(new_processed_image_path)

                # LAP
                # 写入到数据库中
                tool_db.update_image_lap(image_id, str(lap))
                # 保存在当前list中
                processed_image_info['lap'] = str(lap)

                # TAU
                # 写入到数据库中
                tool_db.update_image_tau(image_id, str(tau))
                # 保存在当前list中
                processed_image_info['tau'] = str(tau)

        # 展示图像在面板上
        tool_image.set_image_by_label(processed_image_info['processed_image'], self.__ui.label_processed_image)
        # 展示图片的信息在列表上
        self.__refresh_info_image(tool_db.dic_to_table_widget_item_list(processed_image_info))

    # 设置中部上方的两个图片
    def __set_others_image(self, uncropped_image_path):
        if uncropped_image_path:
            # 截取中部左侧图片 起点275，80； 大小255
            left_image_temp = tool_image.crop_image_by_path(uncropped_image_path, 275, 80, 275+255, 80+255)
            left_temp_save_path = settings.temp_left_image_dir
            tool_image.save_image_to_dir(left_image_temp, left_temp_save_path)
            left_image = QPixmap(left_temp_save_path)
            # 截取中部右部侧图片 起点952，95； 大小72 230
            right_image_temp = tool_image.crop_image_by_path(uncropped_image_path, 952, 95, 952+72, 95+230)
            right_temp_save_path = settings.temp_right_image_dir
            tool_image.save_image_to_dir(right_image_temp, right_temp_save_path)
            right_image = QPixmap(right_temp_save_path)

            # 设置图片在相应的label上
            tool_image.set_image_by_label(left_image, self.__ui.label_left_image, 240, 240)
            tool_image.set_image_by_label(right_image, self.__ui.label_right_image, 80, 240)
        else:
            # 设置图片在相应的label上
            tool_image.set_image_by_label(settings.source_empty_left_image, self.__ui.label_left_image)
            tool_image.set_image_by_label(settings.source_empty_right_image, self.__ui.label_right_image)

    # 刷新图像所产生的基本信息在界面中部板上
    def __refresh_info_image(self, item_list):
        # tool_log.debug("__refresh_info_image", item_list)
        # LAP
        item = item_list['lap']
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.__ui.table_image_info.setItem(7, 1, item)
        # TAU
        item = item_list['tau']
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.__ui.table_image_info.setItem(7, 3, item)
        # MV[eas] & IAS[eas]
        self.__refresh_mv_ias(item_list)

    # 更新mv以及ias属性
    def __refresh_mv_ias(self, item_list):
        if not settings.inspect_lock:
            mve = item_list['mve']
            mva = item_list['mva']
            mvs = item_list['mvs']
            iase = item_list['iase']
            iasa = item_list['iasa']
            iass = item_list['iass']

            # if not self.image_info_lock:
            mve.setData(Qt.UserRole, "mve")
            mva.setData(Qt.UserRole, "mva")
            mvs.setData(Qt.UserRole, "mvs")
            iase.setData(Qt.UserRole, "iase")
            iasa.setData(Qt.UserRole, "iasa")
            iass.setData(Qt.UserRole, "iass")

            # MV[eas]
            self.__ui.table_image_info.setItem(9, 1, mve)
            self.__ui.table_image_info.setItem(9, 2, mva)
            self.__ui.table_image_info.setItem(9, 3, mvs)
            # IAS[eas]
            self.__ui.table_image_info.setItem(10, 1, iase)
            self.__ui.table_image_info.setItem(10, 2, iasa)
            self.__ui.table_image_info.setItem(10, 3, iass)


    # 设置项目文字
    def __set_item_text(self, row, column, text):
        item = self.__ui.table_image_info.item(row, column)
        item.setText(text)
        self.__ui.table_image_info.setItem(row, column, item)


# 获取mv以及ias列表
    def __get_mv_ias_list(self):
        # MV[eas]
        mve = self.__ui.table_image_info.item(9,1).text()
        mva = self.__ui.table_image_info.item(9,2).text()
        mvs = self.__ui.table_image_info.item(9,3).text()

        # IAS[eas]
        iase = self.__ui.table_image_info.item(10, 1).text()
        iasa = self.__ui.table_image_info.item(10, 2).text()
        iass = self.__ui.table_image_info.item(10, 3).text()

        return {'mve': mve, 'mva': mva, 'mvs': mvs,
                'iase': iase, 'iasa': iasa, 'iass': iass}



    # 刷新患者的基本信息在界面中部板上
    def __refresh_info_patient(self, item_list):
        self.image_info_lock = False
        tool_log.debug("__refresh_info_patient")
        # 日期
        item = item_list['create_date']
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.__ui.table_image_info.setItem(1, 1, item)
        # 编号
        item = item_list['patient_id']
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.__ui.table_image_info.setItem(2, 1, item)
        # 姓名
        item = item_list['name']
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.__ui.table_image_info.setItem(2, 3, item)
        # 性别
        item = item_list['gender']
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.__ui.table_image_info.setItem(3, 1, item)
        # 年龄
        item = item_list['age']
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.__ui.table_image_info.setItem(3, 3, item)
        # 身高
        item = item_list['stature']
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.__ui.table_image_info.setItem(4, 1, item)
        # 体重
        item = item_list['weight']
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.__ui.table_image_info.setItem(4, 3, item)
        # SBP
        item = item_list['sbp']
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.__ui.table_image_info.setItem(5, 1, item)
        # DBP
        item = item_list['dbp']
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.__ui.table_image_info.setItem(5, 3, item)
        # BSA
        item = item_list['bsa']
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.__ui.table_image_info.setItem(6, 1, item)
        # BMI
        item = item_list['bmi']
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.__ui.table_image_info.setItem(6, 3, item)
        self.image_info_lock = True

    # 刷新btn_page_info按钮上的文字
    def __refresh_btn_page_info(self):
        if len(settings.patient_image_list):
            self.__ui.btn_page_info.setText(f"第 {settings.image_index + 1} 张 / 共 {len(settings.patient_image_list)} 张")
        else:
            self.__ui.btn_page_info.setText(f"第 {settings.image_index} 张 / 共 {len(settings.patient_image_list)} 张")


# ============窗体测试程序============
if __name__ == "__main__":  # 用于当前窗体测试
    tool_win.win_test(Win_Index)
