## image_cutter

利用HSV颜色模型，基于OpenCV做图片区域剪裁，并找出剪裁区域在原图中的中心点坐标点。

Cut specially shape from image and the Center point of it base on HSV color model and OpenCV.

## Usage

```Python
# 目标的 bgr 颜色值，请注意顺序
bgr = [40, 158, 31]

# 偏移量
thresh = 30
hsv = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)[0][0]
minHSV = [hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh]
maxHSV = [hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh]
point = find_center_point('opencv-sample-box.png',
                            lower=minHSV,
                            upper=maxHSV,
                            DEBUG=True)
# 中心坐标
print(point)
```