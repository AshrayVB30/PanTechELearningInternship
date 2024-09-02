import cv2

# read the image in grayscale
image = cv2.imread('images/butterfly.png', cv2.IMREAD_GRAYSCALE)

# apply global thresholding
_, thresh_global  = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# display the images
cv2.imshow('ORGINAL IMAGE: ',image)
cv2.imshow('GLOBAL THRESHOLDING ',thresh_global)

# wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

