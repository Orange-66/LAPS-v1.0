# -*- coding: utf-8 -*-
# @Time : 2021/1/24 11:19 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_trans.py
# @Remark : 转换格式类型的工具类
# -----------------------------
import os
from tqdm import *
from PIL import Image

# 所在地址
# UI文件所在路径

ui_dir = '../UI/'
# qrc文件所在路径
qrc_dir = '../Resource/Qrc/'
# png文件所在路径
png_dir = '../Resource/Images/Png/'

# 保存地址
# ui to py文件保存路径-开发
ui_py_dir = '../PyUI/'
# ui to py文件保存路径-测试
ui_py_x_dir = '../PyUI-test/'
# qrc to py文件保存路径
qrc_py_dir = '../Resource/Qrc-py/'
# png to icon文件保存路径
png_icon_dir = '../Resource/Images/Icon/'


# 列出目录下的所有xxx文件
def get_xxx_file_list(file_dir, file_type):
    filename_list = []
    files = os.listdir(file_dir)
    for filename in files:
        if os.path.splitext(filename)[1] == file_type:
            filename_list.append(filename)

    return filename_list


# 把扩展名改为.xxx的文件
def to_xxx_file(file_type, filename, suffix=""):
    return os.path.splitext(filename)[0] + suffix + file_type


# 调用系统命令把UI文件转换成Python文件-开发
def ui_to_py():
    ui_file_list = get_xxx_file_list(ui_dir, ".ui")

    for i in tqdm(range(len(ui_file_list)), ascii=True, desc="Process: "):
        ui_file = ui_file_list[i]

        # 不可直接执行版本-开发
        py_file = to_xxx_file(".py", ui_file)
        cmd = 'pyuic5 {ui_file} -o {py_file}'.format(ui_file=ui_dir + ui_file, py_file=ui_py_dir + py_file)

        os.system(cmd)


# 调用系统命令把UI文件转换成Python文件-测试
def ui_to_py_x():
    ui_file_list = get_xxx_file_list(ui_dir, ".ui")

    for i in tqdm(range(len(ui_file_list)), ascii=True, desc="Process: "):
        ui_file = ui_file_list[i]

        # 可直接执行版本-测试
        py_file_x = to_xxx_file(".py", ui_file, "_x")
        cmd_x = 'pyuic5 {ui_file} -o {py_file} -x'.format(ui_file=ui_dir + ui_file, py_file=ui_py_x_dir + py_file_x)

        os.system(cmd_x)


# 调用系统命令把UI文件转换成Python文件-开发以及测试
def ui_to_py_both():
    ui_to_py()
    ui_to_py_x()


# 调用系统命令把qrc文件转换成Python文件
def qrc_to_py():
    qrc_file_list = get_xxx_file_list(qrc_dir, ".qrc")

    for i in tqdm(range(len(qrc_file_list)), ascii=True, desc="Process: "):
        qrc_file = qrc_file_list[i]
        py_file = to_xxx_file(".py", qrc_file, "_rc")
        # 不可直接执行版本-开发
        cmd = 'pyrcc5 {qrc_file} -o {py_file}'.format(qrc_file=qrc_dir + qrc_file, py_file=qrc_py_dir + py_file)
        os.system(cmd)


# 把png文件转换成ico文件
def png_to_icon():
    # 获取目录下文件名
    png_file_files = get_xxx_file_list(png_dir, ".png")
    # 图标大小
    size = (256, 256)

    for i in tqdm(range(len(png_file_files)), ascii=True, desc="Process: "):
        png_file = png_file_files[i]
        icon_file = to_xxx_file(".ico", png_file)
        icon = Image.open(png_dir + png_file)
        try:
            # 图标文件保存至icon目录
            path = os.path.join(png_icon_dir, icon_file)
            icon.save(path)
        except IOError:
            print('connot convert :', png_file)


# 将此PyQT项目转换成exe文件
def project_to_exe(project_name="LAPS"):
    # 打包项目
    cmd = 'pyinstaller -F -w ' \
          '-i ../../Resource/Images/Icon/win_logo.ico ' \
          '../main.py ' \
          '--workpath ./EXE/ ' \
          '--specpath ./EXE/ ' \
          '--distpath ./EXE/ ' \
          '--name {project_name} ' \
          '--clean '.format(project_name=project_name)

    os.system(cmd)

    # 删除spec文件
    root_dir = "./EXE/"
    spec_filename = "LAPS.spec"
    if os.path.exists(os.path.join(root_dir, spec_filename)):
        os.remove(os.path.join(root_dir, spec_filename))
    else:
        print(f'没有找到 [{os.path.join(root_dir, spec_filename)}] 文件或文件夹')

    # 删除workspace文件夹
    root_dir = "./EXE/LAPS/"
    if os.path.exists(root_dir):
        files = os.listdir(root_dir)
        for filename in files:
            if os.path.exists(os.path.join(root_dir, filename)):
                os.remove(os.path.join(root_dir, filename))

        os.rmdir(root_dir)
    else:
        print(f'没有找到 [{root_dir}] 文件或文件夹')


# 程序的主入口
if __name__ == "__main__":
    # 调用系统命令把UI文件转换成Python文件-开发
    # ui_to_py()

    # 调用系统命令把UI文件转换成Python文件-测试
    ui_to_py_x()

    # 调用系统命令把UI文件转换成Python文件-开发以及测试
    # ui_to_py_both()

    # 调用系统命令把qrc文件转换成Python文件
    # qrc_to_py()

    # 把png文件转换成ico文件
    # png_to_icon()

    # 将此PyQT项目转换成exe文件
    # project_to_exe()
