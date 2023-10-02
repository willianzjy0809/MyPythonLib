import matplotlib.pyplot as plt
import numpy as np
import cv2


# 读取图片
img = cv2.imread('example.jpg')
# 转换为灰度图像
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('result1.jpg', gray_img)

f = np.fft.fft2(gray_img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))

cv2.imwrite('result2.jpg', magnitude_spectrum)


plt.subplot(121),plt.imshow(gray_img, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])



plt.show()

# Test
