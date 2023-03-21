import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
lights = [21, 20, 16, 12]
i = 0

while True:
  for i in range(4):
    GPIO.output(lights[i], GPIO.HIGH)
  for i in range(4):
    GPIO.output(lights[i], GPIO.LOW)
    time.sleep(0.25)
  for i in range(4):
    GPIO.output(lights[i], GPIO.HIGH)
    time.sleep(0.25)
