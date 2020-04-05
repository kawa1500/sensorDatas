import board
import digitalio
from pms7003 import Pms7003Sensor, PmsSensorException
import time
from datetime import datetime
import os
import logging
import smbus2
import bme280

def setup(port, file, bme, pms):
	bus = smbus2.SMBus(port)
	calibration = bme280.load_calibration_params(bus, bme)
	pms_sensor = Pms7003Sensor(pms)
	logging.basicConfig(filename=file, filemode='a',format='%(message)s')
	return bus, calibration, pms_sensor

def bme_sample(bus, address, calibration):
	try:
		data = bme280.sample(bus, address, calibration)
		return round(data.temperature,2), round(data.humidity,2), round(data.pressure,2)
	except:
		return -99,-99,-99

def pms_sample(pms):
	data = pms.read()
	return data['pm1_0'], data['pm2_5'], data['pm10']

def log(pm1,pm2,pm10,t,h,p):
	now = datetime.now()
	logging.warning(str(now)+"\t"+str(pm1)+"\t"+str(pm2)+"\t"+str(pm10)+"\t"+str(t)+"\t"+str(h)+"\t"+str(p))


if __name__ == '__main__':
	# Cons data for program
	FILE_NAME = '/home/pi/app.log'
	PORT_BUS=1
	BME_ADDRESS = 0x76
	PMS_ADDRESS = '/dev/serial0'
	LOOP_TIME = 60

	#Setup before start measure
	bus, calibration,pms = setup(PORT_BUS, FILE_NAME, BME_ADDRESS, PMS_ADDRESS)

	while True:
		try:
			pm1,pm2,pm10 = pms_sample(pms)
			t,h,p = bme_sample(bus,BME_ADDRESS,calibration)
			print("zapis")
			print(pm2)
			log(pm1,pm2,pm10,t,h,p)
			time.sleep(LOOP_TIME)
		except:
			print('Other problem')
	pms.close()
