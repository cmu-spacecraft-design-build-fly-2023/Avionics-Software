import board
import analogio

ain5 = analogio.AnalogIn(board.AIN5)

# measure the voltage at pin AIN5 (raw 16-bit value)
raw_ain5 = ain5.value
print(raw_ain5)

# to see what the raw value is scaled from 0V to 3.3V
scaled_ain5 = (ain5.value * 3.3) / (2 ** 16)
print(scaled_ain5 )
