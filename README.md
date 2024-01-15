# 图像处理函数
### 图像抖动函数：
```python
from imageprocessing import ImageHandel
image = Image.open("1.jpg")   
ih = ImageHandel(image) 
# direction: 移动位置：l左，r右，t上，d下，lt左上，rt右上，ld左下，rd右下
# pixel: 移动的像素
ih.move(direction="l", pixel=200)
```

### 图像切片：
```python
from imageprocessing import SplitImage
image = Image.open("1.jpg")   
si = SplitImage(image)
# 按mark矩阵切割图片碎片
mark = (128, 128)
tiles = si.split(mark)
print(tiles)
...
```