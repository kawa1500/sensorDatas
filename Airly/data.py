import io
import logging
import time

lastApp = '-99';
lastAir = '-99';

logging.basicConfig(filename='/home/pi/data.csv', filemode='a', format='%(message)s')

while True:
	with open('/home/pi/app.log', 'r') as f:
		lines = f.read().splitlines()
		lastApp = lines[-1]
		print lastApp
	
	with open('/home/pi/airly.log', 'r') as f:
		lines = f.read().splitlines()
		lastAir = lines[-1]
		print lastAir
	
	dataText = lastApp + "\t" + lastAir
	print dataText
	logging.warning(dataText)
	time.sleep(600)
