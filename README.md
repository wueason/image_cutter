## image_cutter

利用HSV颜色模型，基于OpenCV做图片区域剪裁，并找出剪裁区域在原图中的中心点坐标点。

Cut specially shape from image and the Center point of it base on HSV color model and OpenCV.

## Usage

```Python
# 目标的 bgr 颜色值，请注意顺序
bgr = [40, 158, 31]
point = find_center_point('opencv-sample-box.png',
                            blue_green_red=bgr,
                            DEBUG=True)
# 中心坐标
# point: [((152.0, 152.0), (63.99999237060547, 61.99999237060547), -0.0)]
print(point[0][0][0])
```