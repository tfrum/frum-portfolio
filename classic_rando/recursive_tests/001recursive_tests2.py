import matplotlib.pyplot as plt

def koch_curve(x, y, length, angle, depth):
    if depth == 0:
        plt.plot([x, x + length], [y, y], 'b-')
    else:
        koch_curve(x, y, length/3, angle, depth-1)
        x += length/3
        y += length/3 * np.tan(angle)
        koch_curve(x, y, length/3, -angle, depth-1)
        x += length/3
        y -= length/3 * np.tan(angle)
        koch_curve(x, y, length/3, angle, depth-1)
        x += length/3
        koch_curve(x, y, length/3, -angle, depth-1)

import numpy as np
plt.figure()
koch_curve(0, 0, 1, np.pi/3, 4)
plt.axis('equal')
plt.show()