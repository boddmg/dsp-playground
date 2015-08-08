from matplotlib import pyplot as plt
import numpy as np
import math
import pickle
from scipy import signal

def main():
    # get data
    meta_data = pickle.load(open("meta_data.pkl", "rb"))
    y = np.load("data.pkl")

    fs = meta_data["sample_rate"]
    time = len(y)/fs # in seconds
    x = np.arange(0, time, 1/fs)

    # Add the noise
    # y = y.clip(-10, 7)
    # y += (np.sin(x * 5) * 2).clip(-0.3, 0.8)
    # y += np.random.uniform(size=len(y))

    plt.subplot(231)
    plt.plot(x, y, 'r')

    plt.subplot(232)
    b, a = signal.butter(8, 0.07)
    y_filted = signal.filtfilt(b, a, y)
    plt.plot(x, y_filted, "b")

    plt.subplot(233)
    plt.plot(x, y, "r", x, y_filted, "b")

    plt.subplot(234)
    y = np.abs(np.fft.fft(y))
    f = x[:len(x)/2] *fs / time
    y = y[:len(y)/2]
    plt.plot(f, y)

    plt.subplot(235)
    y = np.abs(np.fft.fft(y_filted))
    y = y[:len(y)/2]
    plt.plot(f, y)

    plt.subplot(236)




    plt.show()

if __name__ == '__main__':
    main()

