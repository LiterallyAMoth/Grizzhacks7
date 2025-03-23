import RPi.GPIO as GPIO # type: ignore
import time

GPIO.setmode(GPIO.BOARD)

ControlPin = [7, 11, 13, 15]

for pin in ControlPin:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin,0)
seq = [ [1, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 1] ]

for i in range (512):
        for fullstep in range (4):
                for pin in range (4):
                    GPIO.output(ControlPin[pin], seq[fullstep][pin])
                time.sleep(0.002)

GPIO.cleanup()