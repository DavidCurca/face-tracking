import cv2
import numpy
s_img = cv2.imread("sharingan.png")
l_img = cv2.imread("python.png")
s_img = cv2.resize(s_img, (30, 30), interpolation = cv2.INTER_AREA)
l_img[0][0] = s_img[0][0]
for i in range(0, 29):
    for j in range(0, 29):
        l_img[i][j] = s_img[i][j]
print(l_img[0][0])
cv2.imshow("Resized image", l_img)
cv2.waitKey(0)
