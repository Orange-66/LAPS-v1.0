# -*- coding: utf-8 -*-
# @Time : 2021/2/5 8:14 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : win_new_single.py
# @Remark : 新建病例-子窗口
# -----------------------------
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QApplication
from PyUI.ui_new_single import Ui_New_Single
from Utils import tool_win, app_info, tool_time, tool_formula


class Win_New_Single(QWidget, Ui_New_Single):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.setupUi(self)  # 构造UI界面

        create_date = tool_time.current_datetime()
        self.line_create_date.setText(create_date)

    @pyqtSlot(str)
    def on_spin_stature_textChanged(self, string):
        # print("on_line_stature_textChanged", string)
        self.refresh_bmi_bsa()

    @pyqtSlot(str)
    def on_spin_weight_textChanged(self, string):
        # print("on_line_weight_textChanged", string)
        self.refresh_bmi_bsa()

    @pyqtSlot()
    # 完成按钮-点击-槽函数
    def on_btn_done_clicked(self):
        # print("on_btn_done_clicked")
        # 获取窗口所有信息
        create_date = self.line_create_date.text()
        patient_id = self.line_id.text()
        name = self.line_name.text()
        gender = self.combo_gender.currentText()
        age = self.spin_age.value()
        stature = self.spin_stature.value()
        weight = self.spin_weight.value()
        bsa = self.spin_bsa.value()
        bmi = self.spin_bmi.value()
        bmi_degree = self.label_degree.text()
        sbp = self.spin_sbp.value()
        dbp = self.spin_dbp.value()
        print(create_date, patient_id, name, gender, age, stature, weight, bsa, bmi, bmi_degree, sbp, dbp)
        self.close()

    @pyqtSlot()
    # 取消按钮-点击-槽函数
    def on_btn_cancel_clicked(self):
        # print("on_btn_cancel_clicked")
        self.close()

    # 更行bmi与bsa在面板中的数值
    def refresh_bmi_bsa(self):
        try:
            self.spin_bmi.setValue(tool_formula.formula_bmi(
                int(self.spin_stature.value()), int(self.spin_weight.value())
            ))
            self.spin_bsa.setValue(tool_formula.formula_bsa(
                int(self.spin_stature.value()), int(self.spin_weight.value())
            ))
            self.label_degree.setText(tool_formula.formula_bmi_degree(int(self.spin_bmi.value())))
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


# ============窗体测试程序============
if __name__ == "__main__":
    tool_win.win_test(Win_New_Single)
