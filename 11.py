import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)


for i1 in range(3):
    for i2 in leds:
        GPIO.output(i2, 1)
        time.sleep(0.2)
        GPIO.output(i2, 0)
        
GPIO.output(leds, 0)
GPIO.cleanup()
