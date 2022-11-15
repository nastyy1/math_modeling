import numpy as np


g = 9.8
x0 = 0
y0 = 3
v0 = 5

alpha = 30 * np.pi / 180
vx0 = v0 * np.cos(alpha)
vy0 = v0 * np.cos(alpha)

t = np.arange(0, 5, 0.01)
x = x0 + vx0 * t
y = y0 + vy0 * t - g * t**2 / 2
print(y)