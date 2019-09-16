# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:31:48 2019

@author: user
"""

#数字化妆类
import face_recognition
from PIL import Image, ImageDraw

#加载图片
image = face_recognition.load_image_file("img\Face_recongnition\\GYY.jpg")

#标识脸部特征
face_landmarks_list = face_recognition.face_landmarks(image)

for face_landmarks in face_landmarks_list:
    #对矩阵转换为图片
    pil_image = Image.fromarray(image)
    #创建绘制对象
    d = ImageDraw.Draw(pil_image,'RGBA')
    
    #绘制眉毛
    d.polygon(face_landmarks['left_eyebrow'],fill = (50, 50, 50, 128))
    d.polygon(face_landmarks['right_eyebrow'], fill=(50, 50, 50, 128))
    d.line(face_landmarks['left_eyebrow'], fill=(50, 50, 50, 128), width=1)
    d.line(face_landmarks['right_eyebrow'], fill=(50, 50, 50, 128), width=1)

    # 绘制嘴唇
    d.polygon(face_landmarks['top_lip'], fill=(100, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(100, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(100, 0, 0, 64), width=1)
    d.line(face_landmarks['bottom_lip'], fill=(100, 0, 0, 64), width=1)

    # 绘制眼睛
    d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 10))
    d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 10))
    
    #绘制眼线
    d.line(
        face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]],
        fill=(0, 0, 0, 110),
        width=1)
    d.line(
        face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]],
        fill=(0, 0, 0, 110),
        width=1)
    
    pil_image.show()
    
    
    
    
    
