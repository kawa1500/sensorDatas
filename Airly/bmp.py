import board
import digitalio
import busio
import time
import adafruit_bme280

i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bme280.Adafruit_BME280_I2C(i2c,0x76)

bmp280.seaLevelhPa = 1013.25

while True:
	print(bmp280.temperature)
	print(bmp280.pressure)
	print(bmp280.altitude)
	time.sleep(10)
