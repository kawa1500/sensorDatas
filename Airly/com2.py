import board
import digitalio
import busio
import adafruit_bme280
from pms7003 import Pms7003Sensor, PmsSensorException
import time
from datetime import datetime
import os
import logging

if __name__ == '__main__':
	sensor = Pms7003Sensor('/dev/serial0')
	i2c = busio.I2C(board.SCL, board.SDA)
	bmp280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, 0x76)
#	file = open("/root/stats.log","a")
	logging.basicConfig(filename='app.log', filemode='a', format='%(message)s')

	while True:
		try:
			print("\n")
			czas = datetime.now()
			print(czas)
			readDataSmog = sensor.read()
			print(readDataSmog)
			time.sleep(10)
			temp = bmp280.temperature
			print(temp)
			logging.warning(str(czas)+"\t"+str(readDataSmog['pm1_0'])+"\t"+str(readDataSmog['pm2_5'])+"\t"+str(readDataSmog['pm10'])+"\t"+str(temp))
#			time.sleep(10)
#			temp = bmp280.temperature
#			print(temp)
#			print(bmp280.pressure)
#			print(bmp280.altitude)
			time.sleep(600)
		except PmsSensorException:
			print('Connection problem')
		except:
			print('Other problem')
	sensor.close()
#	file.close()
