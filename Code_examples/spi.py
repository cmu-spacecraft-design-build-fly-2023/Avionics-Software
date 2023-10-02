from pycubed import cubesat
from adafruit_bme280 import basic as adafruit_bme280

# Setup the SPI device
bme280 = adafruit_bme280.Adafruit_BME280_SPI(cubesat.spi, cs)

print("\nTemperature: %0.1f C" % bme280.temperature)
print("Humidity: %0.1f %%" % bme280.humidity)
print("Pressure: %0.1f hPa" % bme280.pressure)
