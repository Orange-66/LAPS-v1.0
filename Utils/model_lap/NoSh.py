# coding=utf-8
from PIL import Image
import pytesseract
import numpy as np
import cv2


def img2dict(image_path):
    picdict = {"y_cord": "",  # cm/s还是m/s
               "x_cord": "",  # 75mm/s还是150mm/s
               "y1": "",
               "y2": "",
               "y3": "",
               "y4": "",
               }

    img1 = Image.open(image_path)
    img1 = img1.convert('L')
    mat = np.array(img1)
    if mat.shape[0] != 768:
        raise Exception("输入图像尺寸的不是1024x768")

    def access_pixels(image):
        height, width = image.shape

        for row in range(height):
            for list in range(width):
                pv = image[row, list]
                image[row, list] = 255 - pv

        (thresh, image) = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)  # 反色后再取黑白
        cv2.imwrite("AfterDealAndBinary.jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 95])

        return image

    btm = img1.crop((700, 700, 1100, 900))
    y_axis = img1.crop((965, 340, 1100, 700))  # 可以识别出100 200 300，但不能识别cm/s。考虑通过坐标像素值的差值计算出原点坐标

    btm.save("btm.jpg")
    btmSeg = cv2.imread('btm.jpg')
    btm_grayImage = cv2.cvtColor(btmSeg, cv2.COLOR_BGR2GRAY)  # 转化为灰度图像

    y_axis.save("y_axis.jpg")
    ySeg = cv2.imread("y_axis.jpg")
    y_grayImage = cv2.cvtColor(ySeg, cv2.COLOR_BGR2GRAY)

    (thresh, btm_blackAndWhiteImage) = cv2.threshold(btm_grayImage, 225, 255, cv2.THRESH_BINARY)
    (thresh, y_blackAndWhiteImage) = cv2.threshold(y_grayImage, 225, 255, cv2.THRESH_BINARY)  # 转化为黑白二值图像

    cv2.destroyAllWindows()
    btm_final = access_pixels(btm_blackAndWhiteImage)  # 把图片反色，tesseract假定图片是白底黑字，而数据集图片为黑底白字
    y_final = access_pixels(y_blackAndWhiteImage)  # 把图片反色，tesseract假定图片是白底黑字，而数据集图片为黑底白字

    btm_data = pytesseract.image_to_data(btm_final, config="-c tessedit_char_whitelist=0123456789cm/sbp.*")

    y_data = pytesseract.image_to_data(y_final, config="-c tessedit_char_whitelist=0123456789cm/sbp.*")

    def findvalueandposition(target, context, x_bias=0, y_bias=0):  # 寻找data中的目标，还有目标的位置。如果传入了偏移量，则在输出的时候计算偏移后的的坐标
        context_lines = context.split("\n")
        target_line = ""
        foundTarget = False
        for i in range(len(context_lines)):
            if target in context_lines[i]:
                target_line = context_lines[i]
                foundTarget = True
        if not foundTarget:
            raise Exception("Target not found!")
        # print "包含target的那一行是"
        # print target_line

        context_words = target_line.split()
        # print "context_words: "
        # print context_words
        target_dict = {"value": context_words[11], "left": int(context_words[6]) + x_bias,
                       "top": int(context_words[7]) + y_bias,
                       "width": int(context_words[8]), "height": int(context_words[9])}
        # print "target_dict: "
        # print target_dict

        return target_dict

    picdict["x_cord"] = findvalueandposition("m/s", btm_data, 70, 70)  # 可以找到以m/s或者mm/s为单位的文本

    measuredByMS = True

    try:
        picdict["y1"] = findvalueandposition("1.0", y_data, 965, 340)  # 先假设是以m/s度量的
    except:
        print("1.0 not found, trying 100")  # 如果没有1.0，说明不是以m/s为单位
        measuredByMS = False
        picdict["y1"] = findvalueandposition("100", y_data, 965, 340)  # 开始寻找100, 200等
        picdict["y2"] = findvalueandposition("200", y_data, 965, 340)
        picdict["y3"] = findvalueandposition("300", y_data, 965, 340)
        picdict["y4"] = findvalueandposition("400", y_data, 965, 340)

    else:
        picdict["y2"] = findvalueandposition("2.0", y_data, 965, 340)
        picdict["y3"] = findvalueandposition("3.0", y_data, 965, 340)
        picdict["y4"] = findvalueandposition("4.0", y_data, 965, 340)

    y_cord_dict = {}  # 利用提取的坐标值确定范围，并用坐标值的位置算出原点坐标
    if measuredByMS:
        y_cord_dict['value'] = "m/s"
    else:
        y_cord_dict['value'] = "cm/s"

    y_cord_dict['left'] = picdict['y1']['left']
    y_cord_dict['top'] = picdict['y1']['top'] - (picdict['y2']['top'] - picdict['y1']['top'])

    picdict['y_cord'] = y_cord_dict

    return picdict

