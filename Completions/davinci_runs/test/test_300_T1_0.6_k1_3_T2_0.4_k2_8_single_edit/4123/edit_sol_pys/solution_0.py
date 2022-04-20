#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl
from scipy.optimize import leastsq


def model(p, x):
    a, b, c = p
    return a*x**2 + b*x + c


def residuals(p, x, y):
    return y - model(p, x)


def fit(x, y):
    p = [1, 1, 1]
    plsq = leastsq(residuals, p, args=(x, y))
    return plsq[0]


def main():
    x = np.linspace(0, 10, 100)
    y = model([1, 2, 3], x)
    yn = y + 0.1*np.random.randn(len(x))
    p = fit(x, yn)
    print(p)
    pl.plot(x, y)
    pl.plot(x, yn, ".k")
    pl.plot(x, model(p, x))
    pl.show()


if __name__ == "__main__":
    main()
