#!/usr/bin/env python
import cv2
import numpy as np

def find_center_point(file, lower=None, upper=None, DEBUG=False):
    result = False
    if not (lower and upper):
        return result
    # 载入图片
    img = cv2.imread(file)

    # 获取图片HSV颜色空间
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 获取遮盖层
    mask = cv2.inRange(hsv, np.array(lower), np.array(upper))

    # 模糊处理
    blurred = cv2.blur(mask, (9, 9))

    # 二进制化
    ret,binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

    # 填充大空隙
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

    # 填充小斑点
    erode = cv2.erode(closed, None, iterations=4)
    dilate = cv2.dilate(erode, None, iterations=4)

    # 查找轮廓
    _, contours, _ = cv2.findContours(
        dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    i = 0
    for con in contours:
        # 轮廓转换为矩形
        rect = cv2.minAreaRect(con)
        if DEBUG:
            # 矩形转换为box对象
            box=np.int0(cv2.boxPoints(rect))

            # 计算矩形的行列起始值
            y_right = max([box][0][0][1], [box][0][1][1],
                          [box][0][2][1], [box][0][3][1])
            y_left  = min([box][0][0][1], [box][0][1][1],
                          [box][0][2][1], [box][0][3][1])
            x_right = max([box][0][0][0], [box][0][1][0],
                          [box][0][2][0], [box][0][3][0])
            x_left  = min([box][0][0][0], [box][0][1][0],
                          [box][0][2][0], [box][0][3][0])

            if y_right - y_left > 0 and x_right - x_left > 0:
                i += 1
                # 裁剪目标矩形区域
                temp = img[y_left:y_right, x_left:x_right]
                cv2.imshow('target_'+str(i), temp)

            print('rect: {}'.format(rect))
            print('y: {},{}'.format(y_left, y_right))
            print('x: {},{}'.format(x_left, x_right))

    if DEBUG:
        cv2.imshow('origin', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return i > 0

if __name__ == '__main__':
    # 目标的 bgr 颜色值，请注意顺序
    # 左边的绿色盒子
    bgr = [40, 158, 31]

    # 右边的绿色盒子
    # bgr = [40, 158, 31]

    # 偏移量
    thresh = 30
    hsv = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)[0][0]
    minHSV = [hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh]
    maxHSV = [hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh]
    point = find_center_point('opencv-sample-box.png',
                                lower=minHSV,
                                upper=maxHSV,
                                DEBUG=True)
    print(point)