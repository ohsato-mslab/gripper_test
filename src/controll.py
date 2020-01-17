# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import String
import numpy as np
import math
import message_filters
from Sensor.msg import forcereading

def main():
    #初期設定
    rospy.init_node('gripper_controller', anonymous=True)
    #loop = rospy.Rate(0.5)#0.5Hz
    sub1 = message_filters.Subscriber('force_sensor_right', forcereading)
    sub2 = message_filters.Subscriber('force_sensor_left', forcereading)
    gripper_array = np.array([0, 0.73, 1.46, 2.19, 2.92, 3.65, 4.38, 5.11, 5.84, 6.57, 7.34, 8.07, 8.80, 9.53, 10.26,
                    11.00, 11.70, 12.45, 13.18, 13.91, 14.68, 15.41, 16.14, 16.87, 17.80, 18.33, 19.06, 19.79,
                    20.52, 21.25, 22.71, 23.50],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
                    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
                    ##"00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111", "01000",
                    ##"01001", "01010", "01011", "01100", "01101", "01110", "01111", "10000", "10001", "10010", "10011", "10100", "10101",
                    ##"10110", "10111", "11000", "11001", "11010", "11011", "11100", "11101", "11110", "11111"])

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)#17-INLOCK
    GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)#27-START
    GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)#19-POS4
    GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)#22-POS3
    GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)#13-POS2
    GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)#10-POS1
    GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)#11-POS0

    fps = 100.#切り捨てを避けるため敢えて明示的にfloat型
    delay = 1/fps*0.5
    ts = message_filters.ApproximateTimeSynchronizer([sub1,sub2], 10, delay)

    #####  先に制御用電源をON  ####
    try:
        while True:
            now = rospy.Time.now()
            print(now)
            grip()
    except KeyboardInterrupt:
        GPIO.cleanup()

def grip():
    GPIO.output(17,GPIO.HIGH)#INLOCK解除
    print"inlock unlocked"
    ts.registerCallback(callback)
    rospy.sleep(1)
    GPIO.output(27, GPIO.HIGH)#START信号]
    print"start"
    rospy.sleep(1)
    rospy.spin()

def callback(right, left):
    force = right.value + left.value
    wide = 5#forceから求める式に変更予定
    position = getNearestValue(gripper_array[0,:], wide))#何要素目が最も近い把持幅か
    print(position)

    if gripper_array[1, position] == 1 :
        GPIO.output(19,GPIO.HIGH)
    else:
        GPIO.output(19,GPIO.LOW)

    if gripper_array[2, position] == 1 :
        GPIO.output(22,GPIO.HIGH)
    else:
        GPIO.output(22,GPIO.LOW)

    if gripper_array[3, position] == 1 :
        GPIO.output(13,GPIO.HIGH)
    else:
        GPIO.output(13,GPIO.LOW)

    if gripper_array[4, position] == 1 :
        GPIO.output(10,GPIO.HIGH)
    else:
        GPIO.output(10,GPIO.LOW)

    if gripper_array[5, position] == 1 :
        GPIO.output(26,GPIO.HIGH)
    else:
        GPIO.output(26,GPIO.LOW)

def getNearestValue(list, num):
    idx = np.abs(np.asarray(list) - num).argmin()
    print(idx)
    return idx #list[idx]

if __name__ == "__main__" :
    main()
