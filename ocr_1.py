# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:13:14 2019

@author: user
"""

from PIL import Image
import pytesseract
import cv2
import matplotlib.pyplot as plt


path = "img\OCR\\1.jpg"
#image = cv2.imread(path)
image = plt.imread(path)
fig = plt.figure("show picture")

#ax = fig.add_subplot(111)
#ax.imshow(image)
#ax.set_title("OCR源图")
#以灰度图显示图片, 对彩色图像没有作用
##ax.imshow(image,cmap= 'gray')
# 直接显示一张图片,是使用下面这种方法,等效于之前操作ax的4条语句
plt.imshow(image)



#plt.axis('off') # 不显示刻度

plt.show()

text = pytesseract.image_to_string(Image.open(path),lang = "chi_sim")
#cv2.imshow("image",image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()  # 释放所有的窗体资源
print(text)

