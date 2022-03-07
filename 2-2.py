import RPi.GPIO as GPIO
import time

def dec_2bin(number):
    arr = [int(x) for x in bin(number)[2:]]
    arr = [0] * (8 - len(arr)) + arr
    return arr


dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

arr_izm = [255, 127, 64, 32, 5, 0]
for val in arr_izm:
    number = dec_2bin(val)
    GPIO.output(dac, number)
    time.sleep(2)
    GPIO.output(dac, 0)
    
GPIO.output(dac, 0)
GPIO.cleanup()
