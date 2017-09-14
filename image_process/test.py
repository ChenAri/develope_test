import cv2 
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('detecting_blur_result_001.jpg')
#442
#1404
scale = 1
delta = 0
ddepth = cv2.CV_16S
laplacian = cv2.Laplacian(img,cv2.CV_64F).var()
print(laplacian)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Gradient-X
grad_x = cv2.Sobel(gray,ddepth,1,0,ksize = 3, scale = scale, delta = delta,borderType = cv2.BORDER_DEFAULT)
#grad_x = cv2.Scharr(gray,ddepth,1,0)

# Gradient-Y
grad_y = cv2.Sobel(gray,ddepth,0,1,ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)
#grad_y = cv2.Scharr(gray,ddepth,0,1)

abs_grad_x = cv2.convertScaleAbs(grad_x)   # converting back to uint8
abs_grad_y = cv2.convertScaleAbs(grad_y)


dst = cv2.addWeighted(abs_grad_x,0.5,abs_grad_y,0.5,0).var()
print(dst)
#print cv2.var(dst)

# cv2.imshow('dst',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

# plt.show()


# import cv2


# scale = 1
# delta = 0
# ddepth = cv2.CV_16S

# img = cv2.imread('messi5.jpg')
# img = cv2.GaussianBlur(img,(3,3),0)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# # Gradient-X
# grad_x = cv2.Sobel(gray,ddepth,1,0,ksize = 3, scale = scale, delta = delta,borderType = cv2.BORDER_DEFAULT)
# #grad_x = cv2.Scharr(gray,ddepth,1,0)

# # Gradient-Y
# grad_y = cv2.Sobel(gray,ddepth,0,1,ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)
# #grad_y = cv2.Scharr(gray,ddepth,0,1)

# abs_grad_x = cv2.convertScaleAbs(grad_x)   # converting back to uint8
# abs_grad_y = cv2.convertScaleAbs(grad_y)

# dst = cv2.addWeighted(abs_grad_x,0.5,abs_grad_y,0.5,0)
# #dst = cv2.add(abs_grad_x,abs_grad_y)

# cv2.imshow('dst',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()