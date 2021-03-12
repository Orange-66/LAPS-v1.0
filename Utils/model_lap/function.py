from __future__ import division
import os
import sympy
import Utils.model_lap.models as M
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from PIL import Image
from keras.preprocessing.image import array_to_img
import Utils.model_lap.NoSh as N

os.environ["CUDA_VISIBLE_DEVICES"] = "2"


def picture_Preprocess(picture_path):
    if os.path.exists("output"):
        pass
    else:
        os.mkdir("output")

    if os.path.exists("dataset"):
        pass
    else:
        os.mkdir("dataset")

    val = np.ones((2, 392, 448), dtype='float32')

    count1 = 0

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
    image.save('output/original.png')
    np.save('dataset/picture_preprocessed.npy', val)
    return 'dataset/picture_preprocessed.npy'


def edge_Predict(file_path):
    te_data = np.load(file_path)
    output_folder = 'output'

    if os.path.exists(output_folder):
        pass
    else:
        os.mkdir(output_folder)

    model = M.BCDU_net_D3(input_size=(392, 448, 1))
    model.load_weights('model/model_version_2.h5')
    predictions = model.predict(te_data, batch_size=1, verbose=1)
    mat_predicted = np.zeros((392, 896))
    mat_predicted[0:392, 0:448] = predictions[0].reshape(392, 448)
    mat_predicted[0:392, 448:896] = predictions[1].reshape(392, 448)
    image = array_to_img(np.reshape(mat_predicted, (392, 896, 1)))
    image.save(output_folder + '/predicted.png')
    return output_folder + '/predicted.png'


def curve_fit(picture_path, predicted_path):
    predict = N.img2dict(picture_path)

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

        image2 = plt.imread('output/original.png')
        plt.imshow(image2)
        xvals = p1(fit_y)  # 拟合y值

        plt.plot(fit_y, xvals, c='r')

        fit_x = [(i + 340 - origin_x) / x_scale for i in fit_x]
        fit_y = [(i + 40 - origin_y) / y_scale * 0.15 for i in fit_y]

        f1 = np.polyfit(fit_y, fit_x, 2)
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

    plt.scatter(peak_y, peak_x, c='r')

    if os.path.exists("fig"):
        pass
    else:
        os.mkdir("fig")

    fitted_picture_path = 'fig/Figure.png'

    plt.savefig(fitted_picture_path)

    return sum(result_full) / len(result_full) / 3, fitted_picture_path


def process_original_image(original_image):
    file_path = picture_Preprocess(original_image)
    predicted_path = edge_Predict(file_path)
    result, path = curve_fit(original_image, predicted_path)
    return result, path


def process_painting_image(picture_path, predicted_path):
    predict = N.img2dict(picture_path)

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

        image2 = plt.imread('output/original.png')
        plt.imshow(image2)
        xvals = p1(fit_y)  # 拟合y值

        plt.plot(fit_y, xvals, c='r')

        fit_x = [(i + 340 - origin_x) / x_scale for i in fit_x]
        fit_y = [(i + 40 - origin_y) / y_scale * 0.15 for i in fit_y]

        f1 = np.polyfit(fit_y, fit_x, 2)
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

    plt.scatter(peak_y, peak_x, c='r')

    if os.path.exists("fig"):
        pass
    else:
        os.mkdir("fig")

    fitted_picture_path = 'fig/Figure.png'

    plt.savefig(fitted_picture_path)

    return sum(result_full) / len(result_full) / 3, fitted_picture_path
