# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

# 设置参数
sigma = 10.0
beta = 8.0 / 3.0
rho = 28.0

# 定义洛伦兹方程
def lorenz(state, t):
    x, y, z = state
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z

# 设置起始点和时间点
state0 = [1.0, 1.0, 1.0]
t = np.arange(0.0, 100.0, 0.01)

# 使用odeint函数求解ODE
states = odeint(lorenz, state0, t)

# 绘制洛伦兹曲线
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(states[:, 0], states[:, 1], states[:, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim((-20, 20))
ax.set_ylim((-20, 20))
ax.set_zlim((0, 50))
plt.show()
