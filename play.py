import time

from frame import Frame
from pv_frame import Pv
from battery_frame import Battery

if __name__ == "__main__":
	frames = []
	
	baterry = Battery(40, 16)
	frame = Frame(0, 0, 128, 32)
	frame.components.append(baterry)
	frames.append(frame)

	pv = Pv(32, 18)
	frame = Frame(0, 0, 128, 32)
	frame.components.append(pv)
	frames.append(frame)

	while True:
		for fr in frames:
			fr.show()
			time.sleep(1)
