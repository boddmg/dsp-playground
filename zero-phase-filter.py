from matplotlib import pyplot as plt
import numpy as np
import math
import pickle
from scipy import signal
from numpy.fft import rfft, irfft
from numpy import argmax, sqrt, mean, absolute, arange, log10
from scipy.signal import blackmanharris
import thdn



def main():
    # get data
    meta_data = pickle.load(open("meta_data.pkl", "rb"))
    y = np.load("data.pkl")

    fs = 5000.0
    time = len(y)/fs # in seconds
    x = np.arange(0, time, 1/fs)
    for i in meta_data:
        print(i, meta_data[i])
    print(time)

    # Add the noise
    y = y.clip(-10, 7)
    y += (np.sin(x * 5) * 2).clip (-0.3, 0.8)
    y += np.random.uniform(size=len(y))

    plt.subplot(231)
    plt.plot(x, y, 'r')

    plt.subplot(232)
    b, a = signal.butter(8, 0.05)
    y_filtered = signal.filtfilt(b, a, y)
    print(thdn.thdn(y)[:2])
    print(thdn.thdn(y_filtered)[:2])
    plt.plot(x, y_filtered, "b")

    plt.subplot(233)
    plt.plot(x, y, "r", x, y_filtered, "b")

    plt.subplot(234)
    y = np.abs(np.fft.fft(y))
    end = 30
    f = x[:end]
    f = f * fs / time
    y = y[:end]
    print(f)
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

