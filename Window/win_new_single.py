# -*- coding: utf-8 -*-
# @Time : 2021/2/5 8:14 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : win_new_single.py
# @Remark : 新建病例-子窗口
# -----------------------------
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QApplication
from PyUI.ui_new_single import Ui_New_Single
from Utils import tool_win, settings, tool_time, tool_formula, tool_db


class Win_New_Single(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.__ui = Ui_New_Single()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面

        create_date = tool_time.current_datetime()
        self.__ui.line_create_date.setText(create_date)

    # ========================自动关联槽函数========================
    @pyqtSlot(int)
    def on_spin_stature_valueChanged(self, string):
        tool_win.console_print("on_line_stature_textChanged", string)
        self.__refresh_bmi_bsa()

    @pyqtSlot(float)
    def on_spin_weight_valueChanged(self, string):
        tool_win.console_print("on_line_weight_textChanged", string)
        self.__refresh_bmi_bsa()

    @pyqtSlot()
    # 完成按钮-点击-槽函数
    def on_btn_done_clicked(self):
        # tool_win.console_print("on_btn_done_clicked")
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
        # tool_win.console_print(create_date, patient_id, name, gender, age, stature, weight, bsa, bmi, bmi_degree, sbp, dbp)
        Tool_Db.insert_info(Tool_Db(), patient_id, name, create_date, None,
                            gender, age, stature, weight, sbp, dbp, bsa, bmi, bmi_degree, 0)
        self.close()

    @pyqtSlot()
    # 取消按钮-点击-槽函数
    def on_btn_cancel_clicked(self):
        # tool_win.console_print("on_btn_cancel_clicked")
        self.close()

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

            tool_win.console_print(self.__ui.spin_bmi.value())
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


# ============窗体测试程序============
if __name__ == "__main__":
    tool_win.win_test(Win_New_Single)
