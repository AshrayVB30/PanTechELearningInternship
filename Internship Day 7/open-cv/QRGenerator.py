import cv2
import png
import pyqrcode

# string which represent the qr code
s = 'https://karnatakatourism.org/'

# generate QR Code
url = pyqrcode.create(s)

# create and save the svg file naming
url.svg('images/myqr.svg', scale=8)

# create and save the svg file naming
url.png('images/qrcode.png', scale=9)

qr_code = cv2.imread('images/qrcode.png')
cv2.imshow(' QR CODE', qr_code)
cv2.waitKey(0)
cv2.destroyAllWindows()