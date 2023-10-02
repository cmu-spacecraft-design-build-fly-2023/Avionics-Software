import board
import analogio

def scale_vout(target_voltage):
    return int((target_voltage/3.3) * 0xFFFF)

dac = analogio.AnalogOut(board.DAC0)

dac.value = scale_vout(1.65) # output 1.65V
