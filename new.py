#include "opencv2/featu"

import cv2
import os

###### $$$$$$ 函数的封装  一个展示图片的函数疯转
def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# cv2.imshow("lesson", img3ChaCom)
# cv2.waitKey(0)
# cv2.destroyAllWindows()  #销毁系统内注册的窗口程序


# img = cv2.imread("D:/BYP_PYTHON\IMA\EX2.jpg")
# img3ChaCom = cv2.imread('EX2.jpg', 1)

# path = 'D:/BYP_PYTHON/IMA/EX2.jpg'
# path = 'EX2.jpg'
# img3ChaCom = cv2.imread('path', 1)

img3ChaCom = cv2.imread('IMA1/EX2.jpg', 1)  # 使用灰度图方式打开  0     使用BGR方式打开 1
print(img3ChaCom.shape)  # img3ChaCom.shape  画面的图像BGR通道数
print(img3ChaCom.size)  # img3ChaCom.size  画面的图像总像素 BGR空间有三幅画面  灰度只有一副

# cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2) #画一个框出来  （图，起点，终点，未知，画图的线大小）
cv2.rectangle(img3ChaCom, (5, 5), (100, 100), (0, 200, 0), 1)
# gray = cv2.cvtColor(img3ChaCom,cv2.COLOR_BGR2GRAY)   #将图片进行灰度转换   彩色RGB变成黑白
cv_show("lesson", img3ChaCom)

# cat = img3ChaCom[0:100, 100:300]  # 截取某部分图像
# cv_show("lesson1", cat)


# 色彩通道提取 #####################################################################

b, g, r = cv2.split(img3ChaCom)  # 分离图像通道
cv_show("lesson1", g)
img = cv2.merge((g, b, r))  # 合并通道图像   (b,g,r) 正确顺序
cv_show("lesson1", img)

"""
cur_img = img3ChaCom.copy()  # 复制一个画面
cur_img[:, :, 0] = 0  # B
# cur_img[:,:,1]=0  #G
# cur_img[:,:,2]=0  #R  去除某个通道的信息
cv_show("lesson1", cur_img)
"""
# 色彩通道提取 #####################################################################


# cv2.imwrite("IMA1/ex.jpg", img3ChaCom)       #保存图像在某个位置
# cv2.imshow('IMREAD_UNCHANGED+Color',img3ChaCom)


os.system('pause')
