import RPI.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
try: 
 while True:
  GPIO.output(21,GPIO.HIGH)
  sleep(1)
  GPIO.output(21,GPIO.LOW)
  sleep(1)
finally
   GPIO.cleanup();
