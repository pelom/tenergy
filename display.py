#display.py

import gaugette.ssd1306
import gaugette.platform
import gaugette.gpio

import time
import sys
import math
from vector2D import Vector2D

from gaugette.fonts import arial_16
from gaugette.fonts import arial_24
from gaugette.fonts import arial_32

from enum import Enum

class Font(Enum):
	BIG = arial_32
	SMALL = arial_16
	MEDIUM = arial_24

class Align(Enum):
	LEFT 			= 1
	RIGHT			= 2
	CENTER 			= 3
	MODAL  			= 4
	LEFT_CENTER  	= 5
	RIGHT_CENTER  	= 6
	LEFT_BOTTOM  	= 7
	RIGHT_BOTTOM  	= 8
	CENTER_BOTTOM 	= 9

# Define which GPIO pins the reset (RST) and DC signals on the OLED display are connected to on the
# Raspberry Pi. The defined pin numbers must use the WiringPi pin numbering scheme.
RESET_PIN 	= 15 # WiringPi pin 15 is GPIO14.
DC_PIN 		= 16 # WiringPi pin 16 is GPIO15.

spi_bus 	= 0
spi_device 	= 0

class Display (object):

	def __init__(self,  rows=32, cols=128, buffer_cols=256):
		self.rows = rows
		self.cols = cols
		self.buffer_cols = buffer_cols
		self.gpio = gaugette.gpio.GPIO()
		self.spi = gaugette.spi.SPI(spi_bus, spi_device)

		# Change rows & cols values depending on your display dimensions.
		self.led = gaugette.ssd1306.SSD1306(self.gpio, self.spi, reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=rows, cols=cols, buffer_cols=buffer_cols)
		self.FONT = arial_24
		self.FONT_16 = arial_16
		self.FONT_24 = arial_24

	def init(self):
		self.led.begin()
		self.led.clear_display()
		self.led.display()

	def blink(self,  number, delay):
		for i in range(0, number):
			self.led.invert_display()
			time.sleep(delay)
			self.led.normal_display()
			time.sleep(delay)

	def setString(self, text, font, align):
		width = self.led.text_width(text, font)

		point = self.definePoint(align, width, font)
		print 'Point: ', point

		self.led.clear_block(point.x, point.y, self.buffer_cols, self.rows)
		textSize = self.led.draw_text3(point.x, point.y, text, font)
		self.led.display()

		if(width > self.cols):
			margin = 5
			deplay = 0.06
			diff = (width - self.cols)
			self.leftText(diff + margin, deplay)
			self.rightText(diff + margin, deplay)

	def definePoint(self, align, width, font):
		print 'definePoint() align: ', align
		one = 1

		point = self.definePointX(align, width, font, one)
		if (point != None):
			return point

		point = self.definePointXY(align, width, font, one)
		if (point != None):
			return point

		point = self.definePointY(align, width, font, one)
		if (point != None):
			return point

		return Vector2D(0, 0)

	def definePointX(self, align, width, font, one):
		posX = 0
		posY = 0

		if (align == Align.CENTER and width < self.cols):
			posX = self.center(width, 'cols')

		elif (align == Align.RIGHT and width < self.cols):
			posX = (width - self.cols) * - one

		elif (align == Align.LEFT_CENTER):
			posY = self.center(font.char_height, 'rows')

		elif (align == Align.LEFT_BOTTOM):
			posY = (self.rows - font.char_height) + one

		else: return None

		return Vector2D(posX, posY)

	def definePointXY(self, align, width, font, one):
		cols = 'cols'
		rows = 'rows'
		posX = 0
		posY = 0

		if(width >= self.cols): return None
		if (align == Align.MODAL):
			posX = self.center(width, cols)
			posY = self.center(font.char_height, rows)

		elif (align == Align.RIGHT_CENTER):
			posX = (width - self.cols) * -one
			posY = self.center(font.char_height, rows)

		elif (align == Align.RIGHT_BOTTOM):
			posX = (width - self.cols) * -one
			posY = (self.rows - font.char_height) + one

		elif (align == Align.CENTER_BOTTOM):
			posX = self.center(width, cols)
			posY = (self.rows - font.char_height) + one

		else: return None

		return Vector2D(posX, posY)

	def definePointY(self, align, width, font, one):
		rows = 'rows'
		posY = 0

		if(width < self.cols): return None

		if (align == Align.MODAL):
			posY = self.center(font.char_height, rows)

		elif (align == Align.RIGHT_CENTER):
			posY = self.center(font.char_height, rows)

		elif (align == Align.RIGHT_BOTTOM):
			print align
			posY = (self.rows + font.char_height) + one

		elif (align == Align.CENTER_BOTTOM):
			posY = (self.rows - font.char_height) + one

		else: return None

		return Vector2D(0, posY)

	def leftText(self, length, deplay):
		print 'leftText() length: ', length
		for scroll in range(0, length):
			self.led.col_offset = scroll
			self.led.display()
			time.sleep(deplay)

	def rightText(self, length, deplay):
		print 'rightText() length: ', length
		for scroll in range(0, length):
			self.led.col_offset = length - 1 - scroll
			self.led.display()
			time.sleep(deplay)

	def center(self, width, key):
		return (getattr(self, key) - width) / 2

	def drawFillRectangle(self, x1, y1, width, height):
		for x in range(x1, x1 + width):
			for y in range(y1, y1 + height):
				self.led.draw_pixel(x, y)

	def drawRectangle(self, x1, y1, width, height):
		x2 = x1 + width
		y2 = y1 + height

		pointA = Vector2D(x1, y1)
		pointB = Vector2D(x2, y1)
		pointC = Vector2D(x2, y2)
		pointD = Vector2D(x1, y2)

		pointAll = [ [ pointA, pointB ], [ pointB, pointC ], [ pointC, pointD ], [ pointD, pointA ] ]
		for point in pointAll:
			self.drawLine(point[0].x, point[0].y, point[1].x, point[1].y)

	def drawLine(self, x1, y1, x2, y2):
		vector1 = Vector2D(x1, y1)
		vector2 = Vector2D(x2, y2)

		pointList = vector1.bresenham(vector2)
		for p in pointList:
			self.led.draw_pixel(p[0], p[1])

	def loading(self):
		print 'loading()'
		self.led.clear_display()
		self.setString('Loading...', arial_16,  Align.MODAL)
		self.led.display()
		for x in range(1, self.cols):
#			if(x % 10==0):
#				self.blink(1, 0.1)
			for y in range(1, self.rows):
				self.led.draw_pixel(x, (self.rows)-2)
				self.led.display()
		       		time.sleep(0.0001)

		self.led.clear_display()
		self.led.invert_display()
		self.setString('Loading...', arial_16,  Align.MODAL)
		self.led.display()

		for y in range(0, self.rows):
			for x in range(0, self.cols):
		       		self.led.draw_pixel(x, y)
				self.led.display()
		       		time.sleep(0.0001)

	def __str__(self):
	        return str(self.__class__) + ": " + str(self.__dict__)

	def drawRectangleAngle(self, x, y, w, h, a):
		p1 = Vector2D(x, y)
		p2 = Vector2D(x+w, y)
		p4 = Vector2D(x+g, y-h)
		p3 = Vector2D(x+g + w, y-h)

		display.drawLine(p1.x, p1.y, p2.x, p2.y)
		display.drawLine(p2.x, p2.y, p3.x, p3.y)
		display.drawLine(p3.x, p3.y, p4.x, p4.y)
		display.drawLine(p4.x, p4.y, p1.x, p1.y)

if __name__ == "__main__":
	display = Display()
	display.init()

	while True:
		display.setString('Texto longo', arial_16,  Align.MODAL)
		display.led.draw_text2(0, 0, '--->', 1)
		display.blink(10, 0.1)
#		display.loading();
		display.led.normal_display()
		i = 0
		for name, member in Align.__members__.items():
			print name, member
			i=i+1
			display.setString(i.__str__()*1, arial_16,  member)
			display.led.clear_display()
			#display.led.display()
			time.sleep(1)
