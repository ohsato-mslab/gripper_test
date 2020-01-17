#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import rospy
####  原点から0-10-20-32と開いていくプログラム

#初期設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)#17-INLOCK
GPIO.setup(27, GPIO.OUT)#27-START
GPIO.setup(19, GPIO.OUT)#19-POS4
GPIO.setup(22, GPIO.OUT)#22-POS3
GPIO.setup(13, GPIO.OUT)#13-POS2
GPIO.setup(10, GPIO.OUT)#10-POS1
GPIO.setup(11, GPIO.OUT)#11-POS0

#####  先に制御用電源をON  ####
try:
    while True:
        GPIO.output(17,GPIO.HIGH)
        print "INLOCK is unlocked. 5 seconds sleep.."
        rospy.sleep(5.)
        #ここから位置決め　0番
        GPIO.output(19,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)
        GPIO.output(13,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)#すべてのPOSビットを0に
　　 　  GPIO.output(11, GPIO.LOW)
        now = rospy.Time.now()
        print(now)
        rospy.sleep(0.015)#t1待つ
        now = rospy.Time.now()
        print(now)
        GPIO.output(27,GPIO.HIGH)#実行命令
        print "send Position0. 3 seconds sleep.."
        rospy.sleep(3)
        #ここから位置決め　10番
        GPIO.output(19,GPIO.LOW)
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(13,GPIO.LOW)
        GPIO.output(10,GPIO.HIGH)
        GPIO.output(11,GPIO.LOW)
        rospy.sleep(0.015)#t1待つ
        GPIO.output(27,GPIO.HIGH)#実行命令
        print "send Position10. 3 seconds sleep.."
        rospy.sleep(3)
        #ここから位置決め　20番
        GPIO.output(19,GPIO.HIGH)
        GPIO.output(22,GPIO.LOW)
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(11,GPIO.LOW)#すべてのPOSビットを0に
        rospy.sleep(0.015)#t1待つ
        GPIO.output(27,GPIO.HIGH)#実行命令
        print "send Position20. 3 seconds sleep.."
        rospy.sleep(3)
        #ここから位置決め　31番
        GPIO.output(19,GPIO.HIGH)
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(10,GPIO.HIGH)
        GPIO.output(11,GPIO.HIGH)#すべてのPOSビットを0に
        rospy.sleep(0.015)#t1待つ
        GPIO.output(27,GPIO.HIGH)#実行命令
        print "send Position32. 10 seconds sleep.."
        rospy.sleep(10)

except KeyboardInterrupt:
    GPIO.cleanup()
