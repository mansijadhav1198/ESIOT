import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.IN)
GPIO.setup(5,GPIO.OUT)

while True:
    i=GPIO.input(3)
    if i==1:
        GPIO.output(5,GPIO.HIGH)
        print("Obstacle found")
        time.sleep(0.1)
        GPIO.output(5,GPIO.LOW)
    else:
        print("Obstacle not found")
        time.sleep(0.1)