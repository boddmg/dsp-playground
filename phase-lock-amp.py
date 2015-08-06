from matplotlib import pyplot
import numpy as np
import math

def main():
    x = np.array(range(1000) * 0.01)
    y = np.sin(x)
    pyplot.plot(y)

if __name__ == '__main__':
    main()


