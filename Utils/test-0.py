# -*- coding: utf-8 -*-
# @Time : 2021/2/17 6:51 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : test-0.py
# @Remark : 
# -----------------------------

import sys
import cv2
import os
import numpy as np
# import face_recognition
from PyQt5.QtCore import QTimer
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtWidgets import QApplication, QWidget, \
    QToolTip, QPushButton, QMessageBox, QDesktopWidget, QFileDialog, QColorDialog, QFrame, QLabel
from PyQt5.QtGui import QIcon, QFont, QColor, QImage, QPixmap
# import win32com.client as win
#
# speak = win.Dispatch("SAPI.SpVoice")


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.frame = []
        self.frame_name = []
        self.detectFlag = False  # 检测flag
        self.timer_camera = QTimer()  # 定义定时器
        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        col = QColor(0, 255, 0)

        # 创建一个pushButton并为它设置一个tooltip
        self.picture_btn = QPushButton(self)
        self.picture_btn.setText('读取文件')
        # 移动窗口的位置
        self.picture_btn.move(80, 120)
        # 点击触发事件：读取文件
        self.picture_btn.clicked.connect(self.pictureStart)

        # 设置上传图片文件地址显示位置
        self.picture_label = QLabel(self)
        self.picture_label.setText("读取文件位置")
        # self.center()
        self.picture_label.setFixedSize(300, 20)  # 设置框的长宽
        self.picture_label.move(180, 120)
        # self.picture_label.setStyleSheet("QLabel{border-color:black;border-width:2px;}")
        self.picture_label.setStyleSheet("QLabel{background-color:#cccccc;}")

        # 设置上传图片显示区域
        self.upFileLabel = QLabel(self)
        self.upFileLabel.setText("")
        self.upFileLabel.setFixedSize(400, 400)  # width height
        self.upFileLabel.move(80, 160)
        self.upFileLabel.setStyleSheet("QLabel{background-color:#cccccc;}")

    #   设置居中样式
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def pictureStart(self):
        """ Slot function to start the progamme
            """
        pictureName, _ = QFileDialog.getOpenFileName(self, "Open", "", "*.jpg;;*.png;;All Files(*)")
        print(pictureName)
        if pictureName != "":  # “”为用户取消
            self.frame = cv2.imread(pictureName)
            self.frame_name = pictureName
            print(self.frame_name)
            # self.picture_label = QLabel('%s'%(self.frame_name), self)
            self.timer_camera.start(100)
            self.timer_camera.timeout.connect(self.openFrame)

    def openFrame(self):

        if self.frame != []:
            frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            # if self.detectFlag ==True:
            # print("================",self.frame_name)
            self.picture_label.setText('%s' % self.frame_name)

            height, width, bytesPerComponent = frame.shape
            bytesPerLine = bytesPerComponent * width
            q_image = QImage(frame.data, width, height, bytesPerLine,
                             QImage.Format_RGB888).scaled(self.upFileLabel.width(), self.upFileLabel.height())
            self.upFileLabel.setPixmap(QPixmap.fromImage(q_image))

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "确定要退出吗?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = 0
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())



