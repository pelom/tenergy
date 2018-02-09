import time

from frame import Component
from frame import IconTextComponent
from frame import Rectangle
from frame import Frame

from display import Align
from gaugette.fonts import arial_16
from gaugette.fonts import arial_24
from gaugette.fonts import arial_32

class Battery(IconTextComponent):
	def __init__(self, wid=0, hei=0, title='', text=''):
		print 'Battery.__init__()'
		IconTextComponent.__init__(self, wid, hei, title, text)

		self.widthPole = 3
		self.marginPole = self.widthPole * 2

		x =  self.xMargin() + self.border
		y = self.yMargin() +  self.border + self.widthPole
		wid = self.wMargin() - self.border*2
		hei = self.hMargin() - self.widthPole - self.border*2

		self.body = Rectangle(x, y, wid, hei)

	def draw(self, display):
		print 'Baterry.draw() '
		IconTextComponent.draw(self, display)

		display.drawRectangle(self.body.point.x, 14, self.body.wid, self.body.hei)
		self.drawPole(display, self.body.point.x, 14, self.body.wid, self.body.hei)

		xMargin = 3
		yMargin = 1
		self.drawAnimation(display, self.xMargin(), self.hMargin(), self.body.wid, self.body.hei, 0.2, xMargin, yMargin)

	def drawPole(self, display, posX, posY, wid, hei):
		print 'Baterry.drawPole() '

		y = posY - self.widthPole

		x1 = posX + self.marginPole
		display.drawFillRectangle(x1, y, self.widthPole, self.widthPole)

		x2 = posX + (wid - self.widthPole - self.marginPole)
		display.drawFillRectangle(x2, y, self.widthPole, self.widthPole)

	def drawAnimation(self, display, posX, posY, wid, hei, value, xMargin, yMargin):
		self.drawPerc(display, self.xMargin(), self.hMargin(), self.body.wid, self.body.hei, 0.2, xMargin, yMargin)
		display.led.display()
		time.sleep(0.3)

		self.drawPerc(display, self.xMargin(), self.hMargin(), self.body.wid, self.body.hei, 0.5, xMargin, yMargin)
		display.led.display()
		time.sleep(0.3)

		self.drawPerc(display, self.xMargin(), self.hMargin(), self.body.wid, self.body.hei, 0.75, xMargin, yMargin)
		display.led.display()
		time.sleep(0.3)

		self.drawPerc(display, self.xMargin(), self.hMargin(), self.body.wid, self.body.hei, 1, xMargin, yMargin)
		display.led.display()
		#time.sleep(1)

		#self.drawPerc(display, self.xMargin(), self.hMargin(), self.body.wid, self.body.hei, 0, xMargin, yMargin)
		#display.led.display()

	def drawPerc(self, display, posX, posY, wid, hei, value, xMargin, yMargin):
		y = posY + hei
		n = int(14 * value)

		x = posX + xMargin
		w = wid - (xMargin*2)

		display.led.clear_block(x, posY- self.border, w, hei-2)

		for i in range(2, n, yMargin):
			display.drawFillRectangle(x, y-i, w, 1)

if __name__ == "__main__":
	baterry = Battery(40, 16)

	frame = Frame(x=0, y=0, wid=128, hei=32)
	frame.components.append(baterry)
