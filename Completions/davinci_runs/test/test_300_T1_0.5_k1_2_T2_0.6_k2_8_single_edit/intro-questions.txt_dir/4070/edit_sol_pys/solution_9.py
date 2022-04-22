

import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


def create_plot(t1, t2, n):
    t = np.linspace(t1, t2, n)
    s = f(t)
    plt.plot(t, s)


if __name__ == '__main__':
    create_plot(0, 5, 50)
    plt.show()
