# -*- coding: utf-8 -*-
# @Time : 2021/3/31 10:43 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : win_inspect.py
# @Remark : 
# -----------------------------
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QTableWidgetItem, QMessageBox
from PyUI.ui_inspect import Ui_Inspect
from Utils import tool_log, settings, tool_image, tool_file
from PyQt5.QtCore import pyqtSlot, Qt


class Win_Inspect(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.__ui = Ui_Inspect()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面

    @pyqtSlot()
    # 完成按钮-点击-槽函数
    def on_btn_done_clicked(self):
        tool_log.debug("on_btn_done_clicked")
        # 获取窗口所有信息
        image_list = self.__get_album()
        settings.patient_image_list.clear()
        for image_path in image_list:
            uncropped_image_path = image_path
            uncropped_image = QPixmap(uncropped_image_path)
            cropped_image = tool_image.crop_image_by_path(uncropped_image_path, 42, 342, 42 + 896, 342 + 392)
            original_image_path = tool_file.make_path(settings.temp_dir, 'cropped_image.png')
            tool_image.save_image_to_dir(cropped_image, original_image_path)
            original_image = QPixmap(original_image_path)

            settings.patient_image_list.append({'uncropped_image_path': uncropped_image_path,
                                                'uncropped_image': uncropped_image,
                                                'original_image_path': original_image_path,
                                                'original_image': original_image,
                                                'processed_image_path': '',
                                                'processed_image': ''})
        settings.inspect_lock = True
        settings.win_index.image_info_lock = True
        settings.image_index = 0
        # 刷新主页面列表
        settings.win_index.refresh_image_list()
        self.close()
        dialog_title = "LAPS"
        dialog_info = "添加数据成功！"
        tool_log.debug("on_btn_done_clicked", dialog_info)
        QMessageBox.about(self, dialog_title, dialog_info)

    @pyqtSlot()
    # 取消按钮-点击-槽函数
    def on_btn_cancel_clicked(self):
        tool_log.debug("on_btn_cancel_clicked")
        settings.win_index.image_info_lock = True
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
        tool_log.debug("__new_image_item, 第", row_num, "行的__new_image_item", image_path)
        image_name = tool_file.get_file_name(image_path)
        image_item = QTableWidgetItem(image_name, Qt.DisplayRole)
        image_item.setData(Qt.UserRole, image_path)

        return image_item

    # 获得当前列表中的所有图像对象
    def __get_album(self):
        row_count = self.__ui.wtable_album.rowCount()
        result = []
        for i in range(row_count):
            image_path = self.__ui.wtable_album.item(i, 2).data(Qt.UserRole)
            result.append(image_path)
        print(result)
        return result
