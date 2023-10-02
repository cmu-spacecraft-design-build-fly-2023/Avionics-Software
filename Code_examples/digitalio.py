import board
import digitalio

gpio = digitalio.DigitalInOut(board.PB17)
gpio.switch_to_output()
# set the gpio pin (pin PB17) to 3.3V (high)
gpio.value = True

gpio.switch_to_input()
print(gpio.value) # read logic-high or logic-low conditions
