#display.py

import math
import copy

class Vector2D (object):

	def __init__(self,  x=0, y=0):
		self.x = x;
		self.y = y;

	def sizeSqr(self):
		return self.x * self.x + self.y * self.y

	def size(self):
		return math.sqrt(self.sizeSqr())

	def normalizeMe(self):
		return self.divideMe(self.size())

	def normalize(self):
		return copy.copy(self).normalizeMe();

	def divideMe(self, c):
		f = 1.0 / c
		self.x *= f
		self.y *= f
		return self

	def divide(self, c):
		return copy.copy(self).divideMe(c)

	def addMe(self, other):
		self.x += other.x
		self.y += other.y
		return self

	def angle(self):
		return math.atan2(self.y, self.x)

	def angleBetween(self, other):
		angle = other.angle() - self.angle()
		if (math.fabs(angle) < math.pi):
			return angle
		return (angle + (2 * math.pi if angle < 0 else -2 * math.pi))

	def __str__(self):
	    return str(self.__class__) + ": " + str(self.__dict__)

	def bresenham(self, end):
		x1 = self.x
		y1 = self.y
		x2 = end.x
		y2 = end.y
		dx = x2 - x1
		dy = y2 - y1

		# Determine how steep the line is
		is_steep = abs(dy) > abs(dx)

	    # Rotate line
		if is_steep:
			x1, y1 = y1, x1
			x2, y2 = y2, x2

	    # Swap start and end points if necessary and store swap state
		swapped = False
		if x1 > x2:
			x1, x2 = x2, x1
			y1, y2 = y2, y1
			swapped = True

	    # Recalculate differentials
		dx = x2 - x1
		dy = y2 - y1

	    # Calculate error
		error = int(dx / 2.0)
		ystep = 1 if y1 < y2 else -1

	    # Iterate over bounding box generating points between start and end
		y = y1
		points = []
		for x in range(x1, x2 + 1):
			coord = (y, x) if is_steep else (x, y)
			points.append(coord)
			error -= abs(dy)
			if error < 0:
				y += ystep
				error += dx

	    # Reverse the list if the coordinates were swapped
		if swapped:
			points.reverse()
		return points

if __name__ == "__main__":
	vector = Vector2D(2.0, 2.0)
	vector2 = Vector2D(2.0, 4.0)
	print 'vector: ', vector
	print 'sizeSqr: ', vector.sizeSqr()
	print 'vector.size: ', vector.size()
	print 'vector.normalizeMe: ', vector.normalizeMe()
	print 'vector.angle: ', vector.angle()
	print 'vector.angleBetween: ', vector.angleBetween(vector2)
	print Vector2D(0, 0).bresenham(Vector2D(3, 4))
