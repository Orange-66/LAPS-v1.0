from __future__ import division

import math
import os
import sympy
os.environ["CUDA_VISIBLE_DEVICES"] = "2"
from Utils.model_lap import models as M
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from PIL import Image
from keras.preprocessing.image import array_to_img
from Utils.model_lap import NoSh as N

def picture_Preprocess(picture_path):

    output_folder = 'Database/Temp'

    val = np.ones((2, 392, 448), dtype='float32')

    count1 = 0
    # for i in x:
    image1 = Image.open(picture_path)
    image1 = image1.resize((1024, 768))
    image1 = image1.convert("L")
    mat1 = np.array(image1)
    val[count1] = mat1[340:732, 40:488]
    val[count1 + 1] = mat1[340:732, 488:936]
    count1 += 2
    mat = np.zeros((392, 896))
    mat[0:392, 0:448] = val[0]
    mat[0:392, 448:896] = val[1]
    image = array_to_img(np.reshape(mat, (392, 896, 1)))
    image.save(output_folder + '/original.png')
    np.save(output_folder + '/picture_preprocessed.npy', val)
    return output_folder + '/picture_preprocessed.npy'

def edge_Predict(file_path):
    te_data = np.load(file_path)
    output_folder = 'Database/Temp'

    model = M.BCDU_net_D3(input_size=(392, 448, 1))
    model.load_weights('Utils/model_lap/model_lap.h5')
    predictions = model.predict(te_data, batch_size=1, verbose=1)
    mat_predicted = np.zeros((392, 896))
    mat_predicted[0:392, 0:448] = predictions[0].reshape(392, 448)
    mat_predicted[0:392, 448:896] = predictions[1].reshape(392, 448)
    image = array_to_img(np.reshape(mat_predicted, (392, 896, 1)))
    image.save(output_folder + '/predicted.png')
    return output_folder + '/predicted.png'

def curve_fit(picture_path, predicted_path):
    predict = N.img2dict(picture_path)

    output_folder = 'Database/Temp'

    result_full = []

    origin_y = predict['y_cord']['left'] - 23
    origin_x = predict['y_cord']['top'] + 8

    y_scale = 57
    x_scale = round(((predict['y3']['top'] - predict['y2']['top']) +
                     (predict['y2']['top'] - predict['y1']['top']) +
                     (predict['y1']['top'] - predict['y_cord']['top'])) / 3)

    image_predicted = Image.open(predicted_path)
    mat_predicted = np.array(image_predicted)

    x = []
    y = []
    for j in range(len(mat_predicted[0])):
        for i in range(len(mat_predicted)):
            if mat_predicted[i][j] < 150:
                x.append(i)
                y.append(j)
                break
    peaks = signal.find_peaks(x, height=100, distance=100)

    peak_x = []
    peak_y = []

    for i in peaks[0]:
        peak_x.append(x[i])
        peak_y.append(y[i])

    for i in peaks[0]:
        left = i
        right = i
        window_size = 5

        while True:
            if left - window_size < y[0]:
                break
            if x[left] < 100:
                slope = [abs((x[left - j] - x[left - j - 1]) / (y[left - j] - y[left - j - 1]))
                         for j in range(0, window_size - 1)]
                if sum(slope) < 5:
                    break
            left -= 1

        while True:
            if right + window_size > len(y):
                break
            if x[right] < 100:
                slope = [abs((x[right - j] - x[right - j - 1]) / (y[right - j] - y[right - j - 1]))
                         for j in range(0, window_size - 1)]
                if sum(slope) < 5:
                    break
            right += 1

        fit_x = x[left:right]
        fit_y = y[left:right]

        f1 = np.polyfit(fit_y, fit_x, 6)
        p1 = np.poly1d(f1)

        image2 = plt.imread(output_folder + '/original.png')
        plt.imshow(image2)
        xvals = p1(fit_y)  # 拟合y值
        # plt.scatter(fit_y, fit_x)
        plt.plot(fit_y, xvals, c='r')

        fit_x = [(i + 340 - origin_x) / x_scale for i in fit_x]
        fit_y = [(i + 40 - origin_y) / y_scale * 0.15 for i in fit_y]

        f1 = np.polyfit(fit_y, fit_x, 6)
        p1 = np.poly1d(f1)

        T1 = (p1 - 1).roots
        T2 = (p1 - 2).roots
        T3 = (p1 - 3).roots

        T1.sort()
        T2.sort()
        T3.sort()

        for index in range(0, len(T1)):
            t1 = T1[index]
            t2 = T2[index]
            t3 = T3[index]

            lap = sympy.Symbol('lap')

            if fit_y[0] <= t1.real <= fit_y[-1] and fit_y[0] <= t2.real <= fit_y[- 1] and fit_y[0] <= t3.real <= fit_y[
                -1] \
                    and t1.imag == 0j and t2.imag == 0j and t3.imag == 0j:

                result = sympy.solve(((1 / (lap + 16) - 1 / (lap + 4)) / (1 / (lap + 36) - 1 /
                                                                          (lap + 4)) - (t1 - t2) / (t1 - t3)), lap)

                for i in result:
                    result_full.append(i)

                # result = [i / 3 for i in result]
                # print("LAP predicted by System:")
                # print(result)
    # plt.scatter(y, x)
    plt.scatter(peak_y, peak_x, c='r')

    plt.savefig(output_folder + "/figure.png")
    plt.clf()

    result = sum(result_full) / len(result_full) / 4

    tau = (1 - 2) / math.log((result + 16) / (result + 4))

    try:
        return result, tau, output_folder + "/figure.png"
    except:
        return 0, 0, output_folder + "/figure.png"

def process_original_image(picture_path):

    if os.path.exists("Database"):
        pass
    else:
        os.mkdir("Database")

    if os.path.exists("Database/Temp"):
        pass
    else:
        os.mkdir("Database/Temp")

    file_path = picture_Preprocess(picture_path)
    predicted_path = edge_Predict(file_path)
    result, tau, path = curve_fit(picture_path, predicted_path)
    return result, tau, path


def process_painting_image(painting_image):
    predict = N.img2dict(painting_image)

    result_full = []

    origin_y = predict['y_cord']['left'] - 23
    origin_x = predict['y_cord']['top'] + 8

    y_scale = 57
    x_scale = round(((predict['y3']['top'] - predict['y2']['top']) +
                     (predict['y2']['top'] - predict['y1']['top']) +
                     (predict['y1']['top'] - predict['y_cord']['top'])) / 3)

    image_predicted = Image.open(painting_image)
    mat_predicted = np.array(image_predicted)
    mat_predicted = mat_predicted[342:732, 42:936]

    x = []
    y = []
    for j in range(len(mat_predicted[0])):
        for i in range(len(mat_predicted)):
            if mat_predicted[i][j].all() == 0:
                x.append(i)
                y.append(j)
                break

    peaks = signal.find_peaks(x, height=100, distance=100)

    peak_x = []
    peak_y = []

    for i in peaks[0]:
        peak_x.append(x[i])
        peak_y.append(y[i])

    for i in peaks[0]:
        left = i
        right = i
        window_size = 5

        while True:
            if left - window_size < y[0]:
                break
            if x[left] < 100:
                slope = [abs((x[left - j] - x[left - j - 1]) / (y[left - j] - y[left - j - 1]))
                         for j in range(0, window_size - 1)]
                if sum(slope) < 5:
                    break
            left -= 1

        while True:
            if right + window_size > len(y):
                break
            if x[right] < 100:
                slope = [abs((x[right - j] - x[right - j - 1]) / (y[right - j] - y[right - j - 1]))
                         for j in range(0, window_size - 1)]
                if sum(slope) < 5:
                    break
            right += 1

        fit_x = x[left:right]
        fit_y = y[left:right]

        fitted_x = [(i + 340 - origin_x) / x_scale for i in fit_x]
        fitted_y = [(i + 40 - origin_y) / y_scale * 0.15 for i in fit_y]

        f1 = np.polyfit(fitted_y, fitted_x, 6)
        p1 = np.poly1d(f1)

        T1 = (p1 - 1).roots
        T2 = (p1 - 2).roots
        T3 = (p1 - 3).roots

        T1.sort()
        T2.sort()
        T3.sort()

        for index in range(0, len(T1)):
            t1 = T1[index]
            t2 = T2[index]
            t3 = T3[index]

            lap = sympy.Symbol('lap')

            if fitted_y[0] <= t1.real <= fitted_y[-1] and fitted_y[0] <= t2.real <= fitted_y[-1] and fitted_y[0] <= t3.real <= fitted_y[
                -1] \
                    and t1.imag == 0j and t2.imag == 0j and t3.imag == 0j:

                result = sympy.solve(((1 / (lap + 16) - 1 / (lap + 4)) / (1 / (lap + 36) - 1 /
                                                                          (lap + 4)) - (t1 - t2) / (t1 - t3)), lap)


                for i in result:
                    result_full.append(i)
        fit_x = [i + 342 for i in fit_x]
        fit_y = [i + 42 for i in fit_y]

        f1 = np.polyfit(fit_y, fit_x, 6)
        p1 = np.poly1d(f1)

        image2 = plt.imread(painting_image)
        plt.imshow(image2)
        xvals = p1(fit_y)  # 拟合y值
        plt.plot(fit_y, xvals, c='r')


    plt.scatter([i + 42 for i in peak_y], [i + 342 for i in peak_x], c='r')

    output_folder = 'Database/Temp/'
    fitted_picture_path = 'figure.png'

    plt.savefig(output_folder + fitted_picture_path)


    try:
        result = sum(result_full) / len(result_full) / 4
        tau = (1 - 2) / math.log((result + 16) / (result + 4))
        return result, tau, output_folder + fitted_picture_path
    except:
        return 0, 0, output_folder + fitted_picture_path
