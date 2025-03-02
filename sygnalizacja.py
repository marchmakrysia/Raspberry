import RPi.GPIO as GPIO
from time import sleep
#sygnalizacja swietlna, 3 diody
#gpio16-red gpio20-yellow gpio21-green)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
try: 
 while True:
  GPIO.output(20,GPIO.LOW)  
  GPIO.output(16,GPIO.HIGH)
  sleep(1)
  GPIO.output(20,GPIO.HIGH)
  sleep(1)
  GPIO.output(16,GPIO.LOW)
  GPIO.output(20,GPIO.LOW)
  GPIO.output(20,GPIO.HIGH)
  sleep(1) 
  GPIO.output(21,GPIO.LOW)
  GPIO.output(20,GPIO.HIGH)  
finally:
   GPIO.cleanup();
