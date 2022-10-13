import os
import cv2


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 封装 展示图片
"""  if   else  
key = input()

if key == "g":
    print("adsad", key, "ggg")
else:
    print("gg")
"""
list_1 = [1, 2, 4, 5, 23, 2342, 234]

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

os.system('pause')
