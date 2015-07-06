import sys,os
import cv2
import pylab as plt
import numpy as np
import math
import time
sys.path.append('./piggyphoto')
import piggyphoto 
sys.path.append('../myPys')
import ImageWindow


def make_mask(img_shape,top_left,bottom_right):
	mask = np.zeros(img_shape,np.uint8)
	mask[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]] = 255
	return mask

def reverse_black_white(img):
	return 255 - img

def fill_out_of_bounds(img,top_left,bottom_right,fill_value):
	w,h = img.shape[::-1]
	margin = 30
	img[0:h,0:top_left[0]+margin] = fill_value #fill left side
	img[0:top_left[1]+margin,top_left[0]:w] = fill_value #fill upper side
	img[bottom_right[1]-margin:h,top_left[0]:w] = fill_value # fill lower side
	img[0:h,bottom_right[0] - margin -50:w] = fill_value # fill rest of right side
	return img

def get_matched_coordinates(target_img,templete_img):
	# templete matching
	w,h = templete_img.shape[::-1]
	res = cv2.matchTemplate(target_img,templete_img,eval("cv2.TM_CCOEFF"))
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	top_left = max_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)
	return top_left,bottom_right


def displayImages(images):
	for k,v in images.items() :
		cv2.namedWindow(k, cv2.WINDOW_NORMAL)
	 	imageWindow = ImageWindow.ImageWindow(v)
	 	cv2.resizeWindow(k, imageWindow.width(), imageWindow.height())
	 	#plt.subplot(3,2,i),plt.imshow(v,k)
	 	cv2.imshow(k,v)
	# 	plt.show
	k = cv2.waitKey(0)
	if k == 27:         # wait for ESC key to exit
		cv2.destroyAllWindows()


def closing(img):
	##define kernel
	k = np.ones((15,15),np.uint8)
	return cv2.morphologyEx(img, cv2.MORPH_CLOSE, k,5)




