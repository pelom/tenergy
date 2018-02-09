# -*- coding: iso-8859-15 -*-
import time

from frame import Frame
from pv_frame import Pv
from battery_frame import Battery

if __name__ == "__main__":
	frames = []

	baterryV = Battery(40, 16, 'BATERIA > TENSAO', '11,8V')
	baterryA = Battery(40, 16, 'BATERIA > CORRENTE', '30A')
	baterryW = Battery(40, 16, 'BATERIA > POTENCIA', '100W')

	frame = Frame(0, 0, 128, 32)
	frame.title = 'BATERIA > TENSAO'
	frame.components.append(baterryV)
	frames.append(frame)

	frame = Frame(0, 0, 128, 32)
	frame.title = 'BATERIA > CORRENTE'
	frame.components.append(baterryA)
	frames.append(frame)

	frame = Frame(0, 0, 128, 32)
	frame.title = 'BATERIA > POTENCIA'
	frame.components.append(baterryW)
	frames.append(frame)

	pvV = Pv(32, 18, 'PAINEL > TENSAO', '13,8V')
	pvA = Pv(32, 18, 'PAINEL > CORRENTE', '3,1A')
	pvW = Pv(32, 18, 'PAINEL > POTENCIA', '9,8W')

	frame = Frame(0, 0, 128, 32)
	frame.title = 'PAINEL > TENSAO'
	frame.text = '13,8V'
	frame.components.append(pvV)
	frames.append(frame)

	frame = Frame(0, 0, 128, 32)
	frame.title = 'PAINEL > CORRENTE'
	frame.text = '3,1A'
	frame.components.append(pvA)
	frames.append(frame)

	frame = Frame(0, 0, 128, 32)
	frame.title = 'PAINEL > POTENCIA'
	frame.text = '7,3W'
	frame.components.append(pvW)
	frames.append(frame)

	while True:
		for fr in frames:
			fr.show()
			time.sleep(2)
