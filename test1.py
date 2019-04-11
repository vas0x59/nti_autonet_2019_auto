import socket
import argparse
import time
from time import sleep
import os
import cv2
import math
import operator

def setup_gpio():
    # os.system("sudo pigpiod")  # Launching GPIO library
    time.sleep(1)  # As i said it is too impatient and so if this delay is removed you will get an error
    import pigpio
    ESC = 17
    STEER = 18
    pi = pigpio.pi()
    pi.set_servo_pulsewidth(ESC, 0)
    pi.set_servo_pulsewidth(STEER, 0)
    time.sleep(1)
    # pi.set_servo_pulsewidth(ESC, 1500)
    # time.sleep(1)

    return pi,ESC,STEER

def test_esc(pi, ESC, val):
    max_value = 2000  # Максимальное значение шим
    min_value = 700  # Минимальное значение шим
    # pi.set_servo_pulsewidth(ESC, 0)
    pi.set_servo_pulsewidth(ESC, val)
    

pi, ESC, STEER = setup_gpio()
print("init")
test_esc(pi, ESC, 1500)
time.sleep(1.8)
print("1700")
test_esc(pi, ESC, 1700)

time.sleep(3)
print("stop")
test_esc(pi, ESC, 700)