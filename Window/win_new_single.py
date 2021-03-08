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
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTableWidgetItem, QListWidgetItem, QLabel, QMessageBox
from PyUI.ui_new_single import Ui_New_Single
from Utils import tool_win, settings, tool_time, tool_formula, tool_db, tool_image, tool_file
from Widget.wid_preview import Wid_Preview


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
        tool_win.logging("on_line_stature_textChanged", string)
        self.__refresh_bmi_bsa()

    @pyqtSlot(float)
    # 体重输入框-值改变-槽函数
    def on_spin_weight_valueChanged(self, string):
        tool_win.logging("on_line_weight_textChanged", string)
        self.__refresh_bmi_bsa()

    @pyqtSlot()
    # 完成按钮-点击-槽函数
    def on_btn_done_clicked(self):
        tool_win.logging("on_btn_done_clicked")
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

        tool_win.logging(create_date, patient_id, name, gender, age, stature, weight, bsa, bmi, bmi_degree, sbp, dbp)
        try:
            # 添加到数据库
            tool_db.insert_info(patient_id, name, create_date, None,
                                gender, age, stature, weight, sbp, dbp, bsa, bmi, bmi_degree, 0)
            for image_path in image_list:
                tool_db.insert_image(patient_id, image_path)

            dialog_title = "LAPS"
            dialog_info = "添加数据成功！"

        except Exception as e:
            dialog_title = "LAPS"
            dialog_info = "添加数据出现错误。"
        finally:
            tool_win.logging("on_btn_done_clicked", dialog_info)
            QMessageBox.about(self, dialog_title, dialog_info)
            # 刷新主页面列表
            settings.win_index.refresh_window()
            self.close()

    @pyqtSlot()
    # 取消按钮-点击-槽函数
    def on_btn_cancel_clicked(self):
        tool_win.logging("on_btn_cancel_clicked")
        self.close()

    @pyqtSlot()
    # 添加图片按钮-槽函数
    def on_btn_add_image_clicked(self):
        tool_win.logging("on_btn_add_image_clicked")
        # 打开文件获取路径以及Pixmap对象
        image_path, image_pix = tool_file.open_image(self)
        if not image_path == '':
            # 获得当前表格的行数
            current_row = self.__ui.wtable_album.rowCount()
            # 插入
            self.__ui.wtable_album.insertRow(current_row)
            # 设置单元格中的各个item
            self.__createItemsARow(current_row, image_path, image_pix)

    # ========================手动关联槽函数========================
    # 预览按钮槽函数
    def do_btn_preview_clicked(self, image_pix):
        tool_win.logging("do_btn_preview_clicked")
        settings.wid_preview.label.setPixmap(tool_image.set_image(image_pix, settings.wid_preview))
        settings.wid_preview.show()

    # 删除按钮槽函数
    def do_btn_delete_clicked(self, item):
        tool_win.logging("do_btn_delete_clicked")
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

            tool_win.logging("__refresh_bmi_bsa", self.__ui.spin_bmi.value())
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
        tool_win.logging("__new_btn_preview")
        btn_preview = QPushButton("预览")
        btn_preview.clicked.connect(lambda: self.do_btn_preview_clicked(image_pix))
        return btn_preview

    # 新建删除按钮
    def __new_btn_delete(self, image_item):
        tool_win.logging("__new_btn_delete")
        btn_delete = QPushButton("删除")
        btn_delete.clicked.connect(lambda: self.do_btn_delete_clicked(image_item))
        return btn_delete

    # 新建相片item
    def __new_image_item(self, row_num, image_path):
        tool_win.logging("__new_image_item, 第", row_num, "行的__new_btn_delete")
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
