from skimage.filters import sobel
import cv2

img = cv2.imread('shoreline.jpg', 0)
sobel_img = sobel(img)
cv2.imshow("Original", img)
cv2.imshow("Sobel", sobel_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
