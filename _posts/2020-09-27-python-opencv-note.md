---
title:	python-opencv note
tages:	opencv
---

> 整理一下python-opencv常用操作

1. `cv2.imread('filename'),cv2.imwrite('filename',img),cv2.imshow('show name',img)`

2. `b,g,r=cv2.split(img)` 图像通道分离，但是split少用，因为慢。`img=cv2.merge((b,g,r))`

3. `cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)` 色域转换，这里是BGR转灰度图

4. `cv2.copyMakeBorder(src, top, bottom, left, right, borderType)` 这个是图像填充操作，在做卷积等操作的时候需要的padding就可以用这个函数实现，borderType可以有cv2.BORDER_CONSTANT固定值填充，后面加个value=x这个参数就好了。也可以用cv2.BORDER_DEFAULT默认边框类型填充，用的是取镜像对称的像素填充的。

5. image加减乘除操作，同样size/depth and type的就可以这样操作。可以用`cv2.add(x,y),cv2.sub,x+y`之类

6. `cv2.addWeighted(img1,a,img2,b,bias)`图片混合，混合公式如下$dst=\apha . img1 + \beta . img2 + \gama$ 一般a+b=1混合之后的图片就是加了背景一样的感觉hhh是一种透明效果！

7. `cv2.bitwise_add/or/not/xor`位操作

8. `ret,dst=cv2.threshold(src,thresh,maxval,type可选) `这个用来筛掉图像中的一些噪声，就是比thresh小的都被筛掉了，可以用这个做mask，maxval也可以限制图像里的最大值，type可选，如果用cv2.THRESH_BINARY，dst就是一个二值化图像

9. `edges=cv2.Canny(image,threshold1,threshold2)`低于threshold1的像素会被认为不是边缘，高于threshold2的会认为是边缘。如果在threshold1和threshold2之间的像素点，若与第二步得到的边缘相邻，会被认为是边缘。

