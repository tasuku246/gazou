import cv2
import sys


class ImageWindow:

	def __init__(self,image):
		self.image = image
		self.img_width = image.shape[1]
		self.img_height = image.shape[0]
		screen_res = 1440, 900 #screeen resolution
		scale_width = screen_res[0] / float(self.img_width)
		scale_height = screen_res[1] / float(self.img_height)
		scale = min(scale_width, scale_height)
		self.window_height = int(image.shape[0] * scale)
		self.window_width = int(image.shape[1] * scale)

	def width(self):
		return self.window_width

	def height(self):
		return self.window_height

	def width_size(self):
		return self.img_width

	def height_size(self):
		return self.img_height