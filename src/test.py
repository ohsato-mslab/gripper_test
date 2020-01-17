#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import rospy
from time import sleep
####  INLOCK解除するだけのプログラム  ####

#初期設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)#2-INLOCK
GPIO.setup(27, GPIO.OUT)

#####  先に制御用電源をON  ####
try:
    while True:
        GPIO.output(17,GPIO.HIGH)
        rospy.sleep(4.)
        GPIO.output(27, GPIO.HIGH)
        rospy.sleep(5.)
   	print "INLOCK OK"
except KeyboardInterrupt:
    pass

GPIO.cleanup()

