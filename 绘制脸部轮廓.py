# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:09:57 2019

@author: user
"""

#绘制面部轮廓
import face_recognition
from PIL import Image, ImageDraw

# 将图片文件加载到numpy 数组中
image = face_recognition.load_image_file("img\Face_recongnition\\GYY.jpg")

#查找图像中所有面部的所有面部特征
face_landmarks_list = face_recognition.face_landmarks(image)

for face_landmarks in face_landmarks_list:
    face_features = [ 
            'chin', 'left_eyebrow', 'right_eyebrow', 'nose_bridge', 'nose_tip',
        'left_eye', 'right_eye', 'top_lip', 'bottom_lip'
        ]
    pil_img = Image.fromarray(image)
    d = ImageDraw.Draw(pil_img)
    for face_feature in face_features:
        d.line(face_landmarks[face_feature], fill=(255, 255, 255), width=1)
    pil_img.show()
    