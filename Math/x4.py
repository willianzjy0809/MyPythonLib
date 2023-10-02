# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# ���庯��
def f(x):
    return x ** (1/4) + x**3 + x**2 + x

# ��������
x = np.linspace(0, 20, 100)
y = f(x)

# ����ͼ��
fig, ax = plt.subplots()
ax.plot(x, y)

# ��ӱ�ǩ�ͱ���
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('y=x**(1/4) + x**3 + x**2 + x')

# ��ʾͼ��
plt.show()
