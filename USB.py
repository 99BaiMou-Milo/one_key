import os
import cv2

# 引入库

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    #    b, g, r = cv2.split(frame)
    #    frame = cv2.merge((g, b, r))  # 合并通道图像   (b,g,r) 正确顺序
    frame1 = cv2.fastNlMeansDenoisingColored(
                                              frame,
                                               None,
                                                2,
                                                1,
                                                4,
                                                12
    )

    cv2.namedWindow('Video', cv2.WINDOW_FREERATIO)  # 窗口大小自适应比例
#   cv2.namedWindow('result', cv2.WINDOW_NORMAL)  # 窗口大小可以改变
# cv2.namedWindow('result', cv2.WINDOW_AUTOSIZE)    # 窗口大小不可以改变
# cv2.namedWindow('result', cv2.WINDOW_FREERATIO)   # 窗口大小自适应比例
# cv2.namedWindow('result', cv2.WINDOW_KEEPRATIO)   # 窗口大小保持比例
# cv2.namedWindow('result', cv2.WINDOW_GUI_EXPANDED)    # 显示色彩变成暗色 ps.

cv2.imshow("Video", frame1)

cv2.imshow("Video1", frame)

# 读取内容
if cv2.waitKey(10) == ord("q"):  # ord() 可以返回某字母的 ASIC码
    break

# 随时准备按q退出
cap.release()
cv2.destroyAllWindows()
# 停止调用，关闭窗口

os.system('pause')
