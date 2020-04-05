import serial
import datetime
import time

port = serial.Serial('/dev/serial0', baudrate=9600, timeout=2.0)

def read_pm_line(_port):
	rv = b''
	while True:
		ch1 = _port.read()
		print(ch1)
		if ch1 == b'\x42':
			ch2 = _port.read()
			if ch2 == b'\x4d':
				rv += ch1+ch2
				rv += _port.read(28)
				return rv

loop=0

while True:
	rcv = read_pm_line(port)
	print(rcv)
	time.sleep(5)
