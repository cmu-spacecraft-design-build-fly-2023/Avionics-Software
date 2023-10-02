from pycubed import cubesat
import time

while True:
	cubesat.RGB = (0,255,0)
	time.sleep(0.5)
	cubesat.RGB = (0,0,0)
	time.sleep(0.5)
