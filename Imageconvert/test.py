import cv2
import matplotlib.pyplot as plt
# 读取图片
img = cv2.imread('example.jpg')

# 转换为灰度图像
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# 显示图像
plt.imshow(gray_img)
plt.show()
