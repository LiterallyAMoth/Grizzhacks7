import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

buzzer = 16

GPIO.setup(buzzer, GPIO.OUT)
GPIO.output(buzzer, 1)
# testing code to not be too loud
time.sleep(0.005)
GPIO.output(buzzer, 0)