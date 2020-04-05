import board
import digitalio
from pms7003 import Pms7003Sensor, PmsSensorException
import time
from datetime import datetime
import os
import logging
import smbus2
import bme280

if __name__ == '__main__':
	FILE_NAME = 'app.log'
	port=1
	address = 0x76
	bus = smbus2.SMBus(port)
	calibration_params = bme280.load_calibration_params(bus, address)
	sensor = Pms7003Sensor('/dev/serial0')
#	bmp280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, 0x76)
#	file = open("/root/stats.log","a")
	logging.basicConfig(filename=FILE_NAME, filemode='a', format='%(message)s')

	while True:
		try:
#			print("\n")
			czas = datetime.now()
#			print(czas)
			readDataSmog = sensor.read()
#			print(readDataSmog)
			time.sleep(10)
			data = bme280.sample(bus, address, calibration_params)
			temp = data.temperature
			hum = data.humidity
			pre = data.pressure
#			print(temp)
			logging.warning(str(czas)+"\t"+str(readDataSmog['pm1_0'])+"\t"+str(readDataSmog['pm2_5'])+"\t"+str(readDataSmog['pm10'])+"\t"+str(temp)+"\t"+str(hum)+"\t"+str(pre))
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
