#encoding:UTF-8
import numpy
import cv2

# 图片
# img=cv2.imread('test.jpg',0)
# 窗口样式
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# 图片展示
# cv2.imshow('image',img)
# 图片展示时间，0无限
# k = cv2.waitKey(0)
# 关闭图片
# cv2.destroyAllWindows()

# drawing-functions  画图
# 画板
# img = numpy.zeros((512, 512, 3), numpy.uint8)
# 线
# cv2.line(img, (0, 0), (511, 511), (255, 0, 255), 12)
# 矩形
# cv2.rectangle(img,(384,0),(510,128),(0,255,0),-1)
# 圆形
# cv2.circle(img,(447,63), 63, (0,0,255), -1)
# 椭圆形
# cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
# 放数组
# pts = numpy.array([[10,5],[20,30],[70,20],[50,10]], numpy.int32)
# pts = pts.reshape((-1,1,2))
# 带不规则的线
# cv2.polylines(img,[pts],True,(0,255,255))
# 字体
# font = cv2.FONT_HERSHEY_SIMPLEX
# 画字
# cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
# cv2.imshow('image',img)
# k = cv2.waitKey(0)
# cv2.destroyAllWindows()

# 调色板
def nothing(x):
    pass

# 窗口
img = numpy.zeros((100,512,3), numpy.uint8)
cv2.namedWindow('image')

# 进度条的大小
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# 开关
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()