import RPi.GPIO as GPIO
import time
import subprocess
from datetime import datetime

def checkProces(p1,p2,v):
	proc1 = subprocess.Popen(p1, stdout=subprocess.PIPE)
	proc2 = subprocess.Popen(p2, stdin=proc1.stdout,stdout=subprocess.PIPE)
	proc1.stdout.close()
	out = proc2.communicate()
	outF = format(out)
	return v in str(outF)

def checkP(p1,v):
	proc = subprocess.Popen(p1, stdout=subprocess.PIPE)
	out = proc.communicate()
	outF = format(out)
	return v in str(outF)

def debug(fname,com1,com2,airl):
	now = datetime.now()
	print(str(now)+"\t"+fname+"\t"+str(com1)+"\t"+str(com2)+"\t"+str(airl))

if __name__== "__main__":
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(23,GPIO.OUT)
	GPIO.setup(24,GPIO.OUT)
	GPIO.output(23,GPIO.LOW)
	GPIO.output(24,GPIO.LOW)

	while True:
		GPIO.output(24,GPIO.HIGH)

		resultCom = checkProces(['ps', 'aux'],['grep','com4'],"root/Airly/com4.py")
		resultCom2 = not checkP(['tail','/home/pi/app.log','-n','1'],"-99")
		resultAirly = checkProces(['ps','aux'],['grep','example'],"root/Airly/airly_lib/example.py")
		debug("MAIN",resultCom,resultCom2,resultAirly)

		if resultCom and resultCom2 and resultAirly:
			GPIO.output(23,GPIO.LOW)
		else:
			GPIO.output(23,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(24,GPIO.LOW)
		time.sleep(60)
