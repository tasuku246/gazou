import numpy as np


class Polygon2D:
	def __init__(self,coordinates):
		self.coordinates = coordinates[:,0]

	def number_coordinate(self):
		return len(coordinates)

	def _sort_by_colmun(self,array):
		ind = np.lexsort((array[:,0],array[:,1]))
		sorted = array[ind].copy()
		return sorted

	def _sort_by_row(self,array):
		ind = np.lexsort((array[:,1],array[:,0]))
		sorted = array[ind].copy()
		return sorted



class Square(Polygon2D):
	def __init__(self,coordinates):
		Polygon2D.__init__(self,coordinates)

	def lower_left_coordinate(self):
		coor =  self.coordinates.copy()		
		lower = self._sort_by_colmun(coor)
		lower = lower[2:4] ## select lower 2 coordinate
		lower_left = self._sort_by_row(lower) 
		lower_left = lower_left[0] ## select one lower left coordinate
		return lower_left

	def upper_left_coordinate(self):
		coor =  self.coordinates.copy()		
		lower = self._sort_by_colmun(coor)
		lower = lower[0:2] ## select upper 2 coordinate
		lower_left = self._sort_by_row(lower) 
		lower_left = lower_left[0] ## select one lower left coordinate
		return lower_left


		


class Triangle(Polygon2D):
	def __init__(self,coordinates):
		Polygon2D.__init__(self,coordinates)
	
	def left_side_coordinate(self):
		coor =  self.coordinates.copy()		
		sorted = self._sort_by_row(coor)
		left_side_coordinate = sorted[0] 
		return left_side_coordinate
		