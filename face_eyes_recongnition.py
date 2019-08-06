# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 14:56:37 2019

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 14:03:32 2019

@author: user
"""

# 导入opencv-python
import cv2

# 读入一张图片，引号里为图片的路径，需要你自己手动设置
img = cv2.imread('2.jpg',1)

# 导入人脸级联分类器引擎
face_engine = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_engine = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

# 用人脸级联分类器引擎进行人脸识别，返回的faces为人脸坐标列表，1.3是放大比例，5是重复识别次数
faces = face_engine.detectMultiScale(img,scaleFactor=1.3,minNeighbors=5)

# 对每一张脸，进行如下操作
for (x,y,w,h) in faces:
    # 画出人脸框，蓝色（BGR色彩体系），画笔宽度为2
    #矩形——设置左上顶点和右下顶点，颜色，线条宽度
    #cv2.rectangle(img,(10,10),(30,40),(134,2,34),1)
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    face_area = img[y:y+h, x:x+w]
    eyes = eye_engine.detectMultiScale(face_area)

    for (ex,ey,ew,eh) in eyes:
#        img = cv2.rectangle(face_area,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)
        cv2.rectangle(face_area,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)       

# 在"img2"窗口中展示效果图
cv2.imshow('2',img)
# 监听键盘上任何按键，如有按键即退出并关闭窗口，并将图片保存为output.jpg
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output.jpg',img)
print(faces)