from pycubed import cubesat
import time

while True:
		if cubesat.uart.in_waiting: # check if there's anything in uart buffer
			data = cubesat.uart.read(32) # read at most 32 bytes

			# data is a bytearray, we'll want to convert it to a string
			data_string = ''.join([chr(b) for b in data])
			print(data_string)
		time.sleep(0.1)
