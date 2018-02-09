import time

from frame import Component
from frame import IconTextComponent
from frame import Rectangle
from frame import Frame

from vector2D import Vector2D

from display import Align
from gaugette.fonts import arial_16
from gaugette.fonts import arial_24
from gaugette.fonts import arial_32

class Pv(IconTextComponent):
	def __init__(self, wid=0, hei=0, title='', text=''):
		IconTextComponent.__init__(self, wid, hei, title, text)
		#self.border = True

	def draw(self, display):
		print 'Pv.draw() '
		super(self.__class__, self).draw(display)
		#display.led.draw_text2(0, 0, 'PAINEL > CORRENTE', 1)
		#display.setString('8,88 A ', arial_16,  Align.RIGHT_BOTTOM)

		r = 8
		x1 = 0
		y1 = 30
		x2 = x1 + self.wid
		y2 = y1 - self.hei

		p1 = Vector2D(x1, y1)
		p2 = Vector2D(x2, y1)
		p3 = Vector2D(x2 + r, y2)
		p4 = Vector2D(x1 + r, y2)

		display.drawLine(p1.x, p1.y, p2.x, p2.y)
		display.drawLine(p2.x, p2.y, p3.x, p3.y)
		display.drawLine(p3.x, p3.y, p4.x, p4.y)
		display.drawLine(p4.x, p4.y, p1.x, p1.y)

		x = p1.x + (p4.x - p1.x)/2
		y = p1.y + (p4.y - p1.y)/2

		w = p2.x + (p3.x - p2.x)/2
		z = p2.y + (p3.y - p2.y)/2

		display.drawLine(int(x), int(y), int(w), int(z))

		xt = p1.x + (p2.x - p1.x)/2
		xw = p4.x + (p3.x - p4.x)/2
		display.drawLine(int(xt), int(p1.y), int(xw), int(p4.y))

if __name__ == "__main__":
	pv = Pv(32, 18)
	frame = Frame(x=0, y=0, wid=128, hei=32)
	frame.components.append(pv)
	frame.show()
