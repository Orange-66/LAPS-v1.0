# -*- coding: utf-8 -*-
# @Time : 2021/2/5 8:14 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : win_new_single.py
# @Remark : 新建病例-子窗口
# -----------------------------
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QTableWidgetItem, QMessageBox
from PyUI.ui_new_single import Ui_New_Single
from Utils import settings, tool_win, tool_time, tool_formula, tool_db, tool_image, tool_file, tool_log


class Win_New_Single(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.__ui = Ui_New_Single()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面

        create_date = tool_time.current_datetime()
        self.__ui.line_create_date.setText(create_date)

    # ========================自动关联槽函数========================
    @pyqtSlot(int)
    # 身高输入框-值改变-槽函数
    def on_spin_stature_valueChanged(self, string):
        tool_log.debug("on_line_stature_textChanged", string)
        self.__refresh_bmi_bsa()

    @pyqtSlot(float)
    # 体重输入框-值改变-槽函数
    def on_spin_weight_valueChanged(self, string):
        tool_log.debug("on_line_weight_textChanged", string)
        self.__refresh_bmi_bsa()

    @pyqtSlot()
    # 完成按钮-点击-槽函数
    def on_btn_done_clicked(self):
        tool_log.debug("on_btn_done_clicked")
        # 获取窗口所有信息
        create_date = self.__ui.line_create_date.text()
        patient_id = self.__ui.line_id.text()
        name = self.__ui.line_name.text()
        gender = self.__ui.combo_gender.currentText()
        age = self.__ui.spin_age.value()
        stature = self.__ui.spin_stature.value()
        weight = self.__ui.spin_weight.value()
        bsa = self.__ui.spin_bsa.value()
        bmi = self.__ui.spin_bmi.value()
        bmi_degree = self.__ui.label_degree.text()
        sbp = self.__ui.spin_sbp.value()
        dbp = self.__ui.spin_dbp.value()

        image_list = self.__get_album()

        tool_log.debug(create_date, patient_id, name, gender, age, stature, weight, bsa, bmi, bmi_degree, sbp, dbp)
        try:
            # 添加到数据库
            tool_db.insert_info(patient_id, name, create_date, None,
                                gender, age, stature, weight, sbp, dbp, bsa, bmi, bmi_degree, '×')


            for image_path in image_list:
                # 保存uncropped图片的路径以及文件名
                new_uncropped_name = tool_file.make_filename()
                # 旧文件的文件名
                old_uncropped_name = tool_file.get_filename(image_path)
                # 重命名后的文件名
                uncropped_filename = tool_file.rename_file(old_uncropped_name, new_uncropped_name)
                # 保存uncropped文件的路径名
                uncropped_save_path = tool_file.make_path(settings.image_root_dir, patient_id + "-" + name, "uncropped")
                # uncropped—image保存路径并保存到相应路径上
                uncropped_image_path = tool_file.make_path(uncropped_save_path, uncropped_filename)
                print("123",image_path, uncropped_image_path)
                tool_image.save_image(image_path, uncropped_image_path)

                # 根据uncropped-image的路径，获取到相应的图片，并根据该图片进行剪裁得到original-image图像
                original_image = tool_image.crop_image_by_path(uncropped_image_path, 42, 342, 42 + 896, 342 + 392)
                # 设计original-image的保存的文件名
                new_original_name = tool_file.make_filename()
                # 重命名后的文件名
                original_filename = tool_file.rename_file(old_uncropped_name, new_original_name)
                # 保存original-image文件的路径名
                original_save_path = tool_file.make_path(settings.image_root_dir, patient_id + "-" + name, "original", original_filename)
                tool_image.save_image_to_dir(original_image, original_save_path)
                # 将图片路径保存在数据库中
                tool_db.insert_image(patient_id, uncropped_image_path, original_save_path)

            dialog_title = "LAPS"
            dialog_info = "添加数据成功！"

        except Exception as e:
            dialog_title = "LAPS"
            dialog_info = "添加数据出现错误:" + str(e)
        finally:
            tool_log.debug("on_btn_done_clicked", dialog_info)
            QMessageBox.about(self, dialog_title, dialog_info)
            # 刷新主页面列表
            settings.win_index.refresh_window()
            self.close()

    @pyqtSlot()
    # 取消按钮-点击-槽函数
    def on_btn_cancel_clicked(self):
        tool_log.debug("on_btn_cancel_clicked")
        self.close()

    @pyqtSlot()
    # 添加图片按钮-槽函数
    def on_btn_add_image_clicked(self):
        tool_log.debug("on_btn_add_image_clicked")
        # 打开文件获取路径以及Pixmap对象
        image_path_list, image_pix_list = tool_file.open_image(self)
        for i in range(len(image_path_list)):
            # 获得当前表格的行数
            current_row = self.__ui.wtable_album.rowCount()
            # 插入
            self.__ui.wtable_album.insertRow(current_row)
            # 设置单元格中的各个item
            self.__createItemsARow(current_row, image_path_list[i], image_pix_list[i])

    # ========================手动关联槽函数========================
    # 预览按钮槽函数
    def do_btn_preview_clicked(self, image_pix):
        tool_log.debug("do_btn_preview_clicked")
        settings.wid_preview.label.setPixmap(tool_image.set_image(image_pix, settings.wid_preview))
        settings.wid_preview.show()

    # 删除按钮槽函数
    def do_btn_delete_clicked(self, item):
        tool_log.debug("do_btn_delete_clicked")
        # 根据item得到它对应的行数
        row_num = self.__ui.wtable_album.indexFromItem(item).row()
        self.__ui.wtable_album.removeRow(row_num)

    # ========================自定义函数========================
    # 更行bmi与bsa在面板中的数值
    def __refresh_bmi_bsa(self):
        try:
            self.__ui.spin_bmi.setValue(tool_formula.formula_bmi(
                float(self.__ui.spin_stature.value()), float(self.__ui.spin_weight.value())
            ))
            self.__ui.spin_bsa.setValue(tool_formula.formula_bsa(
                float(self.__ui.spin_stature.value()), float(self.__ui.spin_weight.value())
            ))
            self.__ui.label_degree.setText(tool_formula.formula_bmi_degree(float(self.__ui.spin_bmi.value())))

            tool_log.debug("__refresh_bmi_bsa", self.__ui.spin_bmi.value())
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

    # 添加一条图像项目
    def __createItemsARow(self, row_num, image_path, image_pix):
        # 图片名称
        image_item = self.__new_image_item(row_num, image_path)
        self.__ui.wtable_album.setItem(row_num, 2, image_item)

        # 预览图标
        btn_preview = self.__new_btn_preview(image_pix)
        self.__ui.wtable_album.setCellWidget(row_num, 0, btn_preview)

        # 删除图标
        btn_delete = self.__new_btn_delete(image_item)
        self.__ui.wtable_album.setCellWidget(row_num, 1, btn_delete)

    # 新建预览按钮
    def __new_btn_preview(self, image_pix):
        tool_log.debug("__new_btn_preview")
        btn_preview = QPushButton("预览")
        btn_preview.clicked.connect(lambda: self.do_btn_preview_clicked(image_pix))
        return btn_preview

    # 新建删除按钮
    def __new_btn_delete(self, image_item):
        tool_log.debug("__new_btn_delete")
        btn_delete = QPushButton("删除")
        btn_delete.clicked.connect(lambda: self.do_btn_delete_clicked(image_item))
        return btn_delete

    # 新建相片item
    def __new_image_item(self, row_num, image_path):
        tool_log.debug("__new_image_item, 第", row_num, "行的__new_btn_delete")
        # image_name = tool_file.get_file_name(image_path)
        image_name = image_path
        return QTableWidgetItem(image_name, Qt.DisplayRole)

    # 获得当前列表中的所有图像对象
    def __get_album(self):
        row_count = self.__ui.wtable_album.rowCount()
        result = []
        for i in range(row_count):
            image_path = self.__ui.wtable_album.item(i, 2).text()
            result.append(image_path)

        return result


# ============窗体测试程序============
if __name__ == "__main__":
    tool_win.win_test(Win_New_Single)
