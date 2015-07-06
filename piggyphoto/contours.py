import sys
import cv2
import pylab as plt
import numpy as np


class ImageWindow:

	def __init__(self,image):
		self.image = image
		img_height = image.shape[0]
		img_width = image.shape[1]
		screen_res = 1280, 1024 #screeen resolution
		scale_width = screen_res[0] / img_width
		scale_height = screen_res[1] / img_height
		scale = min(scale_width, scale_height)
		self.window_width = int(image.shape[1] * scale)
		self.window_height = int(image.shape[0] * scale)

	def width(self):
		return self.window_width

	def height(self):
		return self.window_height


if  len(sys.argv) < 2 :
	#print "please specify image file name automatically"
	print "please specify image file name automatically specify imge file name temporary"
	sys.argv.append("IMG_3325.JPG")
	#quit()


img = cv2.imread(sys.argv[1], 0)
img_out = cv2.imread(sys.argv[1], 0)

imageWindow = ImageWindow(img)
canny = cv2.Canny(img,10,30,5)
laplacian = cv2.Laplacian(img,3)
ret,thresh = cv2.threshold(img,130,255,cv2.THRESH_BINARY)
thre_canny = cv2.Canny(thresh,5,3)

contours, hierarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img_out,contours,-1,(0,255,0),3)


images = {'image':img,'canny':canny,'thresh':thresh, 'thre_canny':thre_canny, 'img_out':img_out }
i = 0
for k,v in images.items() :
	cv2.namedWindow(k, cv2.WINDOW_NORMAL)
	cv2.resizeWindow(k, imageWindow.width(), imageWindow.height())
	#plt.subplot(3,2,i),plt.imshow(v,k)
	cv2.imshow(k,v)
	i += 1

	plt.show
		

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()

