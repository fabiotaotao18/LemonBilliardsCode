#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import math
if __name__ == '__main__':
    x=np.linspace(0.0,0.5,50)
    y=np.sin(np.sqrt(x))
    z=np.sqrt(np.sin(x))
    # plt.plot(x,y,"b-",lw=2.5)
    # plt.plot(x,z,"r-",lw=2.5)
    # plt.show()
    # List of coefficient arrays for multiple quadratic equations
    # Each inner list represents the coefficients [a, b, c] for ax^2 + bx + c = 0
    list_of_equations = [
        [1, 3, 2],  # x^2 + 3x + 2 = 0  (roots: -1, -2)
        [1, -6, 9],  # x^2 - 6x + 9 = 0 (root: 3)
        [1, 3, 3]  # x^2 + 3x + 3 = 0 (complex roots)
    ]
    for coefficients in list_of_equations:
        roots = np.roots(coefficients)
        print(f"For coefficients {coefficients}, the roots are: {roots}")

    print(roots[0])