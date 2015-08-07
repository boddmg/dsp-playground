from matplotlib import pyplot as plt
import numpy as np
import math

def main():
    x = np.arange(0, 1, 0.1)
    y = np.sin(x)
    plt.plot(x, y)

if __name__ == '__main__':
    main()
