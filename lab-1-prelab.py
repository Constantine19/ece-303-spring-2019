"""
Lab 1 Prelab

Author:  Konstantin Zelmanovich
Created: 04/01/2019
"""

import numpy as np
import matplotlib.pyplot as plt


def linear_regression(x, y, force_origin=False):
    """
    Performs linear regression given the x-data and y-data
    There should be an option to force the fitted equation through the origin.

    :param x, y: x-data in one list and y-data in another list
    :param force_origin: if True, force fits the equation through the origin
    :return: coefficients b0, b1 and r^2, the coefficient of determination
    """

    if force_origin:
        x = np.insert(x, 0, 0)
        y = np.insert(y, 0, 0)

    # number of points
    n = np.size(x)

    # calculating means
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # calculating b1 and b2
    numer = 0
    denom = 0
    for i in range(n):
        numer += (x[i] - mean_x) * (y[i] - mean_y)
        denom += (x[i] - mean_x) ** 2

    b1 = numer / denom
    b0 = mean_y - (b1 * mean_x)

    # calculating r^2
    ss_t = 0
    ss_r = 0
    for i in range(n):
        y_pred = b0 + b1 * x[i]
        ss_t += (y[i] - mean_y) ** 2
        ss_r += (y[i] - y_pred) ** 2
    r2 = 1 - (ss_r / ss_t)

    return b1, b0, r2


def plot(x, y, b):
    """
    Plots linear regression given the x-data and y-data

    :param x, y: x-data and y-data
    :param b: linear regression b
    :return: none
    """

    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m", marker="o", s=30)

    # predicted response vector
    y_pred = b[0] + b[1] * x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()


def main():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

    b = linear_regression(x, y)
    print ' b1: {}  b2: {} r2: {}'.format(b[0], b[1], b[2])
    plot(x, y, b)


if __name__ == "__main__":
    main()
