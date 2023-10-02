# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# ���庯��
def f(x):
    return 4*x+3*x-x**2-5

# ��������
x = np.linspace(-10, 20, 100)
y = f(x)

# ����ͼ��
fig, ax = plt.subplots()
ax.plot(x, y)

# ��ӱ�ǩ�ͱ���
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('y=4*x+3*x-x**2-5')

# ��ʾͼ��
plt.show()
