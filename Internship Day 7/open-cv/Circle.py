import cv2

image = cv2.imread('images/butterfly.png')

center_coordinates = (150, 100)
radius = 50
color = (255, 0, 0)
thickness = 2

cv2.circle(image, center_coordinates, radius, color, thickness)

cv2.imshow('Image with circle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()