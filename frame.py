from display import Display

from vector2D import Vector2D

class Rectangle(object):
	def __init__(self,  x=0, y=0, wid=0, hei=0):
		self.point = Vector2D(x, y);
		self.wid = wid;
		self.hei = hei;

	def __str__(self):
	    return str(self.__class__) + ": " + str(self.__dict__)

class Component(object):
	def __init__(self,  x=0, y=0, wid=0, hei=0, margin=0):
		self.point = Vector2D(x, y)
		self.wid = wid
		self.hei = hei
		self.margin = margin
		self.border = 0

	def draw(self, display):
		print 'Component.draw() '
		self.clean(display);
		self.drawBorder(display)

	def clean(self, display):
		display.led.clear_block(self.point.x, self.point.y, self.wid+1, self.hei+1)

	def drawBorder(self, display):
		if self.border < 1: return
		x = self.xMargin()
		y = self.yMargin()
		w = self.wMargin()
		h = self.hMargin()
		display.drawRectangle(x, y, w, h)

	def xMargin(self):
		return self.point.x + self.margin
	def yMargin(self):
		return self.point.y + self.margin
	def wMargin(self):
		return self.wid - self.margin * 2
	def hMargin(self):
		return self.hei - self.margin * 2

class Frame(Component):
	def __init__(self,  x=0, y=0, wid=0, hei=0, margin=1):
		super(self.__class__, self).__init__(x, y, wid, hei, margin)
		self.components = []
		self.display = Display()
		self.display.init()

	def draw(self):
		super(self.__class__, self).draw(self.display)

		for component in self.components:
			component.draw(self.display);

		self.display.led.display()
	def show(self):
		self.draw()

#if __name__ == "__main__":
#	frame = Frame(0, 0, 128, 32)
	#frame.components.append(Component(5, 5, 10, 10))
#	frame.show()
