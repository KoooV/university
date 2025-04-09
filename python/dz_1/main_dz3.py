from functools import reduce
from operator import add
import numpy as np


def calculate_iteration(i, j, y):
    base = i**3 + 1 + 76 * j**2
    return base**7 - 98 * y**5 - 55 * j**2


def main(b, m, y):
    y_term = 98 * y**5
    return float(sum(
        pow(i**3 + 1 + 76 * j**2, 7) - y_term - 55 * j**2
        for j in range(1, m + 1)
        for i in range(1, b + 1)
    ))

