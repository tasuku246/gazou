import numpy as np
import cv2
import ImageWindow
import time
import myCV

class ColorDetector:
	def __init__(self,img):
		self.img = img
		##conveert HSV color space
		self.hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		self.hue = self.hsv[:,:,0]
		self.saturation = self.hsv[:,:,1]
		self.meido = self.hsv[:,:,2]


	def detectRed(self,mabiki):
		original_imageWindow = ImageWindow.ImageWindow(self.hue)	
		hue = cv2.resize(self.hue,(original_imageWindow.width_size()/mabiki,original_imageWindow.height_size()/mabiki))
		saturation = cv2.resize(self.saturation,(original_imageWindow.width_size()/mabiki,original_imageWindow.height_size()/mabiki))
		meido = cv2.resize(self.meido,(original_imageWindow.width_size()/mabiki,original_imageWindow.height_size()/mabiki))
		small_imageWindow = ImageWindow.ImageWindow(hue)
		red_image = np.zeros([small_imageWindow.height_size(),small_imageWindow.width_size()],np.uint8)
		hue  = cv2.medianBlur(hue,15) ## apply medial fillter
		#self.saturation = cv2.medianBlur(self.saturation,15) ## apply medial fillter
			

		start = time.time();
		for i,h in np.ndenumerate(hue):
			if (h < 8 or h > 148) and saturation[i[0],i[1]] > 80:
				red_image[i[0],i[1]] = 255
			else:
				red_image[i[0],i[1]] = 0


		closing_img = myCV.closing(red_image)
		closing_img = cv2.resize(closing_img,(original_imageWindow.width_size(),original_imageWindow.height_size()))

		print 'process time',time.time() - start 

		return closing_img




