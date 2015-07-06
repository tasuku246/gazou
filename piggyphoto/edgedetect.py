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
	print "please specify image file name"
	quit()


img = cv2.imread(sys.argv[1], 0)
img_out = cv2.imread(sys.argv[1], 0)

imageWindow = ImageWindow(img)
canny = cv2.Canny(img,50,1exit00,3)
laplacian = cv2.Laplacian(img,3)
ret,thresh = cv2.threshold(img,130,255,cv2.THRESH_BINARY)
thre_canny = cv2.Canny(thresh,5,3)

lines = cv2.HoughLines(canny,2,np.pi/180,100)
for rho,theta in lines[0]:
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a*rho
	y0 = b*rho
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))
	cv2.line(img_out,(x1,y1),(x2,y2),(0,0,255),2)


images = {'image':img,'canny':canny,'thresh':thresh, 'thre_canny':thre_canny, 'hought lines':img_out }
i = 0
for k,v in images.items() :
	cv2.namedWindow(k, cv2.WINDOW_NORMAL)
	cv2.resizeWindow(k, imageWindow.width(), imageWindow.height())
	
	#plt.subplot(2,2,i),plt.imshow(v)

	cv2.imshow(k,v)
	i += 1

plt.show
		

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()

