#!/usr/bin/python2.7
# -*- coding:utf-8 -*-
__author__ = 'gimbu'
__data__ = '06/06/17'

from MVCam_py import MVCam
import cv2
import numpy as np
import sys
import time

if __name__ == '__main__':
    MVCam1 = MVCam()
    if not MVCam1.EnumerateDevice():
        print 'Cannot find any cameras!'
        exit(-1)
    resolution = (1280, 960)
    cam_list = MVCam1.Getname()
    cam_list = cam_list.split(',')
    print '-------------------------------------------------'
    print 'There are all cameras we Found!'
    object = enumerate(cam_list)
    for i, name in object:
        print "%d " % i + name
    cam_name = cam_list[0]
    cv2.namedWindow(cam_name, cv2.WINDOW_AUTOSIZE)
    hCam = MVCam1.Init(cam_name)
    print 'hCam', hCam
    print 'SetImageResolution', MVCam1.SetImageResolution(hCam, resolution[0], resolution[1])
    print 'SetExposureTime', MVCam1.SetExposureTime(hCam, 10000)
    print 'SetTriggerMode', MVCam1.SetTriggerMode(hCam, 1)
    print 'CameraSetTriggerCount', MVCam1.SetTriggerCount(hCam, 1)
    print 'Play', MVCam1.Play(hCam)

    #---------------necessary--------------------
    while True:
        img = MVCam1.getImage(hCam, 1000)
        if img is None:
            break
    #---------------necessary--------------------

    index = 0
    i = 0
    while True:
        exposure_time = [10000, 20000, 30000, 40000, 50000]
        MVCam1.SoftTrigger(hCam)
        img0 = MVCam1.getImage(hCam, 1000)
        # if img0 is None:
        #     continue
        cv2.imshow(cam_name, img0)
        key = chr(cv2.waitKey(5) & 0xff)


        if key in ['s', 'S']:
            cv2.imwrite("./color_edge/0"+str(i)+".png", img0)
            print "saved" + str(i) + "image "
            i += 1
            if i == 10:
                i = 0

        if key in ['q', 'Q']:
            print '\nUnInit', MVCam1.UnInit(hCam)
            break
