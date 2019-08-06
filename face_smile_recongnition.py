# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 15:21:37 2019

@author: user
"""

#导入opencv
import cv2

# 导入人脸级联分类器引擎，'.xml'文件里包含训练出来的人脸特征，cv2.data.haarcascades即为存放所有级联分类器模型文件的目录
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# 导入人眼级联分类器引擎吗，'.xml'文件里包含训练出来的人眼特征
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
# 调用摄像头摄像头
cap = cv2.VideoCapture(0)
while(True):
    # 获取摄像头拍摄到的画面
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, 2, 3)
    img = frame
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
        
        face_area = img[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(face_area,1.5,3)
        for (ex,ey,ew,eh) in eyes:
             cv2.rectangle(face_area,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)
             
       ## 微笑检测
        # 用微笑级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
        smiles = smile_cascade.detectMultiScale(face_area,scaleFactor= 1.16,minNeighbors=65,minSize=(25, 25),flags=cv2.CASCADE_SCALE_IMAGE)
        for (ex,ey,ew,eh) in smiles:
            #画出微笑框，红色（BGR色彩体系），画笔宽度为1
            cv2.rectangle(face_area,(ex,ey),(ex+ew,ey+eh),(0,0,255),1)
            cv2.putText(img,'Smile',(x,y-7), 3, 1.2, (0, 0, 255), 2, cv2.LINE_AA)
    # 展示实时效果
    
    cv2.imshow('frame2',img)
    # 每5毫秒监听一次键盘动作
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
        
        


# 最后，关闭所有窗口
cap.release()
cv2.destroyAllWindows()