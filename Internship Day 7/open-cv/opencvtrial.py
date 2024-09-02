import cv2

img = cv2.imread('images/butterfly.png')

# READ THE IMAGE IN GRAYSCALE
edges = cv2.Canny(img, 100, 200)
cv2.imshow('ORGINAL IMAGE: ',img)
cv2.imshow('CANNY EDGES ',edges)

cv2.waitKey(0)
cv2.destroyAllWindows()