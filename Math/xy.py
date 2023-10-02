# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# 定义函数
def f(x):
    return 4*x+3*x-x**2-5

# 生成数据
x = np.linspace(-10, 20, 100)
y = f(x)

# 创建图形
fig, ax = plt.subplots()
ax.plot(x, y)

# 添加标签和标题
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('y=4*x+3*x-x**2-5')

# 显示图形
plt.show()
