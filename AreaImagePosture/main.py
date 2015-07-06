import sys,os
import cv2
#import pylab as plt
import numpy as np
import math
import time
import serial
sys.path.append('../piggyphoto')
sys.path.append('../myPys')
import piggyphoto 
import myCV
import Polygon2D
import ColorDetector
import ImageWindow
from datetime import datetime as dt


res_dir_name = dt.now().strftime('%Y-%m-%d-%H-%M-%S')
os.mkdir('./result/'+ res_dir_name)
f = open('./result/'+ res_dir_name +'/area.csv','w')
	

def main(filename):
	img = cv2.imread(filename,cv2.CV_LOAD_IMAGE_COLOR)
	cv2.imwrite('res' + filename,img)

	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	hue = hsv[:,:,0]
	saturation = hsv[:,:,1]
	meido = hsv[:,:,2]


	##process
	output_image,binary_img,area = getContactArea(img)

	## image output
	print 'area=',area,'[mm^2]'
	f.write(str(area) + '\t' + filename + '\n')
	cv2.imwrite(filename,img)

	images = {'image':img,'hsv':hsv,'hue':hue,'saturation':saturation,'meido':meido,'red':output_image,'binary':binary_img}
	#images = {'image':img,'ContactArea':output_image}
	myCV.displayImages(images)


def getContactArea(img):
	scale = math.pow((1 / 47.0),2) ## pixel/mm^2

	colorDetecotor = ColorDetector.ColorDetector(img)
	area_img = colorDetecotor.detectRed(3)
	img_for_contour = np.copy(area_img)

	contours= cv2.findContours(img_for_contour,cv2.cv.CV_RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
	areas = [cv2.contourArea(cnt) for cnt in contours]
	cnt_max = [contours[areas.index(max(areas))]] #area max contours is chosen
	cv2.drawContours(img, cnt_max, -1, (0,255,0), 2)
	max_area = areas[areas.index(max(areas))]
	area = max_area * scale
	return img,area_img,area

if __name__ == "__main__":

	if '-c' in sys.argv:
	#if sys.argv[1] == '-c':
		C = piggyphoto.camera()
		print('mesurement...')
		count = 0
		while True:
			print "before wait key"
			k = raw_input("preses 1 key to mesure or press 0 to exit\n")
#			k = cv2.waitKey(0)
			if k == '1':
				print "process is running...\n please wait\n"
				filename = 'images/res' + str(count) +  '.JPG'
				C.capture_image(filename)
				main(filename)
				count = count + 1
				#k = cv2.waitKey(0)
			#	if k == 27:         # wait for ESC key to exit
				
			if k == '0':
				print "process down..."
				break;

	elif '-f' in sys.argv:
		index = sys.argv.index('-f') + 1
		filename = sys.argv[index]
		main(filename)

	else:
		filename = 'images/DSC_0030.JPG'
		main(filename)



