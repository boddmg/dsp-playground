from matplotlib import pyplot as plt
import numpy as np
import math
import pickle
from scipy import signal
from numpy.fft import rfft, irfft
from numpy import argmax, sqrt, mean, absolute, arange, log10
from scipy.signal import blackmanharris
import thdn

def single_frequency_filter(input_signal):
    y_f_all = np.fft.fft(input_signal)
    y_f_all[:10] = np.array([0] *10)
    y_f_half = y_f_all[:len(y_f_all) / 2]
    y_f_abs = np.abs(y_f_half)
    y_f_max = max(y_f_abs)
    y_f_max_index = np.where(y_f_abs == y_f_max)[0][0]
    y_f_all[:y_f_max_index] = [0] * (y_f_max_index)
    y_f_all[y_f_max_index+1:] = [0] * (len(y_f_all)-y_f_max_index-1)
    y_filtered = np.fft.ifft(y_f_all)
    return y_filtered


def main():
    # get data
    meta_data = pickle.load(open("meta_data.pkl", "rb"))
    # y = np.concatenate((np.load("data.pkl")[:256], np.array([0] * (600 - 256))))
    # y = np.concatenate((np.load("data.pkl")[:], [0]*6000))
    y = np.load("data.pkl")[:200]
    y = signal.resample(y, 5000)

    fs = 5000.0 * (10000/200)
    time = len(y)/fs # in seconds
    x = np.arange(0, time, 1/fs)
    # x = x[:-1]
    for i in meta_data:
        print(i, meta_data[i])
    print("time",time)
    end = 1000
    f = x[:end]
    f = f * fs / time

    # Add the noise
    # y = y.clip(-10, 7)
    # y += (np.sin(x * 5) * 2).clip (-0.3, 0.8)
    # y += np.random.uniform(size=len(y))

    plt.subplot(231)
    plt.plot(x, y, 'r')

    plt.subplot(232)
    y_filtered = single_frequency_filter(y)*10
    # filter_function = np.array(([0] * 6 + [1] + [0] * (600 - 7)))
    # filter_function = np.fft.ifft(filter_function)
    # y_filtered = np.fft.ifft(y_f * filter_function)
    # y_filtered = np.convolve(y_filtered, filter_function, mode='same')

    # y_filtered = np.sin(x*np.pi*2*  )*10
    plt.plot(x, y_filtered, "b")

    plt.subplot(233)
    plt.plot(x[:end], y[:end], "r", x[:end], y_filtered[:end], "b")

    plt.subplot(234)
    y = np.abs(np.fft.fft(y))

    y = y[:end]
    plt.plot(f, y)

    plt.subplot(235)
    y_filtered = np.abs(np.fft.fft(y_filtered))
    y_filtered = y_filtered[:end]
    plt.plot(f, y_filtered)

    plt.subplot(236)
    plt.plot(f, y, 'r', f, y_filtered, 'b')
    plt.show()

if __name__ == '__main__':
    main()

