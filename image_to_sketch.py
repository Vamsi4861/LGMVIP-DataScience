import cv2
image = cv2.imread("ironman.jpg")
grey_filter = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

invert = cv2.bitwise_not(grey_filter)
blur=cv2.GaussianBlur(invert,(21,21),-2)
inverted_blur=cv2.bitwise_not(blur)

sketch_filter=cv2.divide(grey_filter,inverted_blur,scale=255.5)

cv2.imwrite("output.png",sketch_filter)
