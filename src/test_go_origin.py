#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import rospy
####  原点復帰プログラム  ####

#初期設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT,initial=GPIO.LOW)#19-POS4
GPIO.setup(27, GPIO.OUT,initial=GPIO.LOW)#3-START
GPIO.setup(13, GPIO.OUT)#13-POS2
GPIO.setup(22, GPIO.OUT)#4-POS3
GPIO.setup(11, GPIO.OUT)#6-POS0
GPIO.setup(10, GPIO.OUT)#17-POS1
GPIO.setup(17, GPIO.OUT)#2-INLOCK


#####  先に制御用電源をON  ####
try:
    while True:
        print"now start"
        GPIO.output(17,GPIO.HIGH)
        rospy.sleep(5.)
        print"sleeped 5 seconds."
        GPIO.output(19,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)
        GPIO.output(13,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(11,GPIO.LOW)#すべてのPOSビットを0に
        rospy.sleep(2.)#待つ
        print"go"
        GPIO.output(27,GPIO.HIGH)#実行命令
        rospy.sleep(5.)

except KeyboardInterrupt:
    GPIO.cleanup()
