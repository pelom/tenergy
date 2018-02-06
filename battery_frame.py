import time
from frame import Component
from frame import Rectangle
from frame import Frame

from display import Align
from gaugette.fonts import arial_16
from gaugette.fonts import arial_24
from gaugette.fonts import arial_32

class Battery(Component):
	def __init__(self, wid=0, hei=0):
		super(self.__class__, self).__init__(0, 0, wid, hei, 0)

		self.widthPole = 3
		self.marginPole = self.widthPole * 2

		x =  self.xMargin() + self.border
		y = self.yMargin() +  self.border + self.widthPole
		wid = self.wMargin() - self.border*2
		hei = self.hMargin() - self.widthPole - self.border*2

		self.body = Rectangle(x, y, wid, hei)

	def draw(self, display):
		print 'Baterry.draw() '
		super(self.__class__, self).draw(display)
		display.led.draw_text2(0, 0, 'BATERIA > TENSAO', 1)
		display.setString('12,8 v ', arial_16,  Align.RIGHT_BOTTOM)
		display.drawRectangle(self.body.point.x, 14, self.body.wid, self.body.hei)
		self.drawPole(display, self.body.point.x, 14, self.body.wid, self.body.hei)
		#self.drawPerc(display, x, y, wid, hei)

		self.drawPerc(display, self.xMargin(), self.hMargin(), self.body.wid, self.body.hei, 0.2)
		display.led.display()
		time.sleep(1)

		self.drawPerc(display, self.xMargin(), self.hMargin(), self.body.wid, self.body.hei, 0.5)
		display.led.display()
		time.sleep(1)

		self.drawPerc(display, self.xMargin(), self.hMargin(), self.body.wid, self.body.hei, 0.75)
		display.led.display()
		time.sleep(1)

		self.drawPerc(display, self.xMargin(), self.hMargin(), self.body.wid, self.body.hei, 1)
		display.led.display()
		time.sleep(1)

	def drawPole(self, display, posX, posY, wid, hei):
		print 'Baterry.drawPole() '

		y = posY - self.widthPole

		x1 = posX + self.marginPole
		display.drawFillRectangle(x1, y, self.widthPole, self.widthPole)

		x2 = posX + (wid - self.widthPole - self.marginPole)
		display.drawFillRectangle(x2, y, self.widthPole, self.widthPole)

	def drawPerc(self, display, posX, posY, wid, hei, value):
		marginX = 3
		marginY = 1

		y = posY + hei
		n = int(14 * value)

		for i in range(2, n, marginY):
			print i
			display.drawFillRectangle(posX + marginX, y-i, wid-(marginX*2), 1)

if __name__ == "__main__":
	baterry = Battery(40, 16)

	frame = Frame(x=0, y=0, wid=128, hei=32)
	frame.components.append(baterry)
