# coding=utf-8
from PIL import Image
import pytesseract
import numpy as np
import cv2
import os

def img2dict(image_path):
    picdict = {"y_cord": "",  # cm/s还是m/s
               "x_cord": "",  # 75mm/s还是150mm/s
               "y1": "",
               "y2": "",
               "y3": "",
               "y4": "",
               }
    btm_left = 700
    btm_upper = 700
    btm_right = 1100
    btm_lower = 900

    y_axis_left = 965
    y_axis_upper = 340
    y_axis_right = 1100
    y_axis_lower = 700

    binary_thresh = 80

    img1 = Image.open(image_path)
    # mat = np.array(img1)
    # print(mat.shape)
    img1 = img1.convert('L')
    mat = np.array(img1)
    if mat.shape[0] == 576:
        print("输入图像尺寸的不是1024x768")
        btm_left = 550
        btm_upper = 500
        btm_right = 650
        btm_lower = 700

        y_axis_left = 695
        y_axis_upper = 300
        y_axis_right = 722
        y_axis_lower = 650

        binary_thresh = 130

    # img1 = img1.resize((1024, 768), Image.ANTIALIAS)
    # mat = np.array(img1)
    # print(mat.shape)

    def access_pixels(image):
        height, width = image.shape
        # print("width:%s,height:%s" % (width, height))
        for row in range(height):
            for list in range(width):
                pv = image[row, list]
                image[row, list] = 255 - pv
        # cv2.imwrite("AfterDeal.jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 95])

        (thresh, image) = cv2.threshold(image, binary_thresh, 255, cv2.THRESH_BINARY)  # 反色后再取黑白
        # cv2.imwrite("AfterDealAndBinary.jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 95])

        return image

    # img1 = convert_to_monochrome(img1)
    btm = img1.crop((btm_left, btm_upper, btm_right, btm_lower))
    # img1 = img1.crop((500, 200, 1100, 900))
    # img1 = img1.crop((700, 700, 1100, 900)) 剪出mm/s & bpm
    y_axis = img1.crop(
        (y_axis_left, y_axis_upper, y_axis_right, y_axis_lower))  # 可以识别出100 200 300，但不能识别cm/s。考虑通过坐标像素值的差值计算出原点坐标

    path = "Database"
    if not os.path.exists(path):
        os.mkdir("Database")

    path = "Database/Temp"
    if not os.path.exists(path):
        os.mkdir("Temp")

    btm.save("Database/Temp/11btm.jpg")
    btmSeg = cv2.imread('Database/Temp/11btm.jpg')
    btm_grayImage = cv2.cvtColor(btmSeg, cv2.COLOR_BGR2GRAY)  # 转化为灰度图像
    cv2.imwrite("Database/Temp/btm_grayImage.jpg", btm_grayImage, [int(cv2.IMWRITE_JPEG_QUALITY), 95])

    y_axis.save("Database/Temp/11y_axis.jpg")
    ySeg = cv2.imread("Database/Temp/11y_axis.jpg")
    y_grayImage = cv2.cvtColor(ySeg, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("Database/Temp/y_grayImage.jpg", y_grayImage, [int(cv2.IMWRITE_JPEG_QUALITY), 95])

    # (thresh, btm_blackAndWhiteImage) = cv2.threshold(btm_grayImage, 120, 255, cv2.THRESH_BINARY)
    # (thresh, y_blackAndWhiteImage) = cv2.threshold(y_grayImage, 225, 255, cv2.THRESH_BINARY)  # 转化为黑白二值图像
    #
    # cv2.imshow('Btm Black white image', btm_blackAndWhiteImage)
    # cv2.imshow('y Black white image', y_blackAndWhiteImage)
    # # cv2.imshow('Original image', originalImage)
    # cv2.imshow('Gray image', grayImage)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # img2 = img2.crop(((10,340,1000,760)))
    btm_final = access_pixels(btm_grayImage)  # 把图片反色，tesseract假定图片是白底黑字，而数据集图片为黑底白字
    cv2.imwrite("Database/Temp/btm_final.jpg", btm_final, [int(cv2.IMWRITE_JPEG_QUALITY), 95])

    y_final = access_pixels(y_grayImage)  # 把图片反色，tesseract假定图片是白底黑字，而数据集图片为黑底白字
    cv2.imwrite("Database/Temp/y_final.jpg", y_final, [int(cv2.IMWRITE_JPEG_QUALITY), 95])

    raw_btm_data = pytesseract.image_to_data(btm_final, config="-c tessedit_char_whitelist=0123456789cm/sbp.*")
    btm_data = raw_btm_data.replace("ms", "m/s")  # 补上没有识别的"/"
    # print("rawbtm:")
    # print(raw_btm_data)
    # print("btm:")
    # print(btm_data)

    raw_y_data = pytesseract.image_to_data(y_final, config="-c tessedit_char_whitelist=0123456789cm/sbp.*")
    y_data = raw_y_data.replace("ms", "m/s")
    # print("rawy:")
    # print(raw_y_data)
    # print("y:")
    # print(y_data)

    # print("y:")
    # print(y_data)

    # # 找关键元素的坐标 在下面封装成了函数
    # btm_lines = btm_data.split("\n")  # 每行字分成String
    # # print("btm_lines[0] = " + btm_lines[0])
    # x_cord_line = ""
    # for i in range(len(btm_lines)):
    #     if "m/s" in btm_lines[i]:
    #         x_cord_line = btm_lines[i]
    # print "包含x单位的那一行是"
    # print x_cord_line
    #
    # btm_words = x_cord_line.split()
    # print "btm_words: "
    # print btm_words
    # x_cord_dict = {"left": btm_words[6], "top": btm_words[7], "width": btm_words[6], "height": btm_words[7]}
    # print "x_cord_dict: "
    # print x_cord_dict

    def findvalueandposition(target, context, x_bias=0, y_bias=0):  # 寻找data中的目标，还有目标的位置。如果传入了偏移量，则在输出的时候计算偏移后的的坐标
        context_lines = context.split("\n")
        target_line = ""
        foundTarget = False
        for i in range(len(context_lines)):
            if target in context_lines[i]:
                target_line = context_lines[i]
                foundTarget = True
        if not foundTarget:
            target_dict = target + " not found"
            return target_dict
        # print "包含target的那一行是"
        # print target_line

        context_words = target_line.split()
        # print "context_words: "
        # print context_words
        target_dict = {"value": context_words[11], "left": int(context_words[6]) + x_bias,
                       "top": int(context_words[7]) + y_bias,
                       "width": int(context_words[8]), "height": int(context_words[9])}
        # print("target_dict: ")
        # print(target_dict)

        return target_dict

    def measuredByMS(context):
        if "100" in context or "200" in context:
            # print( "++++++++++++++100, 200 founded")
            return False
        else:
            return True

    #
    # try:  # 不用分两种情况try catch，直接在输出的结果中替换可能的错误文本
    # print("Looking for x_cord:")
    # picdict["x_cord"] = findvalueandposition("m/s", btm_data, btm_left, btm_upper)  # 可以找到以m/s或者mm/s为单位的文本
    # except:
    #     picdict["x_cord"] = findvalueandposition("ms", btm_data, btm_left, btm_upper)  # 针对不能找出"/"的优化

    # measuredByMS = True

    if measuredByMS(y_data):
        picdict["y1"] = findvalueandposition("1.0", y_data, y_axis_left, y_axis_upper)  # 先假设是以m/s度量的
        picdict["y2"] = findvalueandposition("2.0", y_data, y_axis_left, y_axis_upper)
        picdict["y3"] = findvalueandposition("3.0", y_data, y_axis_left, y_axis_upper)
        picdict["y4"] = findvalueandposition("4.0", y_data, y_axis_left, y_axis_upper)
        picdict["y5"] = findvalueandposition("5.0", y_data, y_axis_left, y_axis_upper)
        picdict["y6"] = findvalueandposition("6.0", y_data, y_axis_left, y_axis_upper)
        picdict["y7"] = findvalueandposition("7.0", y_data, y_axis_left, y_axis_upper)
        picdict["y8"] = findvalueandposition("8.0", y_data, y_axis_left, y_axis_upper)
    else:
        picdict["y1"] = findvalueandposition("100", y_data, y_axis_left, y_axis_upper)  # 开始寻找100, 200等
        picdict["y2"] = findvalueandposition("200", y_data, y_axis_left, y_axis_upper)
        picdict["y3"] = findvalueandposition("300", y_data, y_axis_left, y_axis_upper)
        picdict["y4"] = findvalueandposition("400", y_data, y_axis_left, y_axis_upper)
        picdict["y5"] = findvalueandposition("500", y_data, y_axis_left, y_axis_upper)
        picdict["y6"] = findvalueandposition("600", y_data, y_axis_left, y_axis_upper)
        picdict["y7"] = findvalueandposition("700", y_data, y_axis_left, y_axis_upper)
        picdict["y8"] = findvalueandposition("800", y_data, y_axis_left, y_axis_upper)

    # print("picdict:")
    # print(picdict)

    y_cord_dict = {}  # 利用提取的坐标值确定范围，并用坐标值的位置算出原点坐标
    try:
        if measuredByMS(y_data):
            y_cord_dict['value'] = "m/s"
        else:
            y_cord_dict['value'] = "cm/s"

        y_cord_dict['left'] = picdict['y2']['left']
        y_cord_dict['top'] = picdict['y2']['top'] - (picdict['y4']['top'] - picdict['y2']['top'])


        picdict['y_cord'] = y_cord_dict
    except:
        if measuredByMS(y_data):
            y_cord_dict['value'] = "m/s"
        else:
            y_cord_dict['value'] = "cm/s"

        y_cord_dict['left'] = picdict['y2']['left']
        y_cord_dict['top'] = picdict['y1']['top'] - (picdict['y2']['top'] - picdict['y1']['top'])

        picdict['y_cord'] = y_cord_dict

    return picdict

    # print(a)
    # print(b)
    #
    # print(len(a))
    # print(len(b))


# if __name__ == '__main__':
#     print(img2dict("rename42.jpg"))  # 最后打印处理结果（键是每个元素名字，值都是包含了位置信息和文本的字典的）字典值
#     print("============================================================================================\n"
#           "============================================================================================")
#     print(img2dict("129-023ZHOU LI YONG20201110085317800.jpg"))  # 打印图片中横轴的单位
