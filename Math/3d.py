# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ������������
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# ���㺯��ֵ
Z = np.sin(np.sqrt(X**2 + Y**2))

# ����3Dͼ��
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)

# �����������ǩ
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# ��ʾͼ��
plt.show()
