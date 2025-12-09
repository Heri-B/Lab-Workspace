"""
Lab 15
Bheri
12/8/2025

This program plots a circle on a grid using matplotlib, sine, and cosine.
"""

import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 360)
x = np.cos(theta)
y = np.sin(theta)

plt.figure(figsize=(6, 7))
plt.plot(x, y, label = 'Circle', color = 'blue', linewidth = 2, linestyle = '-')
plt.title('Circle Plot Using Parametric Equations')
plt.xlabel('Cos')
plt.ylabel('Sin')
plt.grid(True, color = 'white')
plt.gca().set_facecolor('lightblue')
plt.gca().set_aspect('equal', adjustable = 'box')

plt.legend()
plt.show()