from MVCam_py import MVCam
import cv2
import numpy as np
import sys
import time

def AeState(pos):
    global hCam
    New = cv2.getTrackbarPos('AeState', cam_name)
    # print pos
    New = True if New else False
    print 'SetAeState', MVCam1.SetAeState(hCam,New)

def AnalogGain(pos):
    global hCam
    New = cv2.getTrackbarPos('AnalogGain', cam_name)
    # print pos
    print 'AnalogGain:', MVCam1.SetAnalogGain(hCam, New)
    # print 'GetAnalogGain', MVCam1.GetAnalogGain(hCam)

def expose(pos):
    global hCam
    Newexpose = cv2.getTrackbarPos('expose', cam_name)
    # print pos
    
    print 'exposeset:', MVCam1.SetExposureTime(hCam, Newexpose)

def AutoWb(pos):
    global hCam
    New = cv2.getTrackbarPos('AutoWb', cam_name)
    # print pos
    New = True if New else False
    print 'AutoWb:', MVCam1.SetWbMode(hCam, New)
    print 'SetOnceWB', MVCam1.SetOnceWB(hCam)

def colorTemp(pos):
    global hCam
    Newred = cv2.getTrackbarPos('red', cam_name)
    Newgreen = cv2.getTrackbarPos('green', cam_name)
    Newblue = cv2.getTrackbarPos('blue', cam_name)
    Newsaturation = cv2.getTrackbarPos('saturation', cam_name)

    print 'SetClrTempMode:', MVCam1.SetClrTempMode(hCam,2)
    print 'SetUserClrTempGain:', MVCam1.SetUserClrTempGain(hCam,Newred,Newgreen,Newblue)
    print 'SetSaturation', MVCam1.SetSaturation(hCam,Newsaturation)
    # print 'SetOnceWB', MVCam1.SetOnceWB(hCam)


def gammacontrast(pos):
    global hCam
    Newgamma = cv2.getTrackbarPos('gamma', cam_name)
    Newcontrast = cv2.getTrackbarPos('contrast', cam_name)
    # print pos
    print 'SetLutMode:', MVCam1.SetLutMode(hCam,0)
    print 'gamma:', MVCam1.SetGamma(hCam, Newgamma)
    print 'contrast:', MVCam1.SetContrast(hCam, Newcontrast)



def Sharpness(pos):
    global hCam
    New = cv2.getTrackbarPos('Sharpness', cam_name)
    # print pos
    print 'Sharpness:', MVCam1.SetSharpness(hCam, New)

def Threshold(pos):
    global hCam
    New = cv2.getTrackbarPos('Threshold', cam_name)
    # print pos
    print 'Threshold:'

def FOV(pos):
    global hCam
    VOffsetFOV = cv2.getTrackbarPos('VOffsetFOV', cam_name)
    HOffsetFOV = cv2.getTrackbarPos('HOffsetFOV', cam_name)
    MVCam1.SetOffsetFOV(hCam, VOffsetFOV, HOffsetFOV)


def getXY(event,x,y,flags,param):
    global x1,y1,x2,y2
    if event==cv2.EVENT_LBUTTONDOWN:
        x1, y1 = x, y
        print("point1:=", x, y)
    elif event==cv2.EVENT_LBUTTONUP:
        print("point2:=", x, y)
        x2, y2 = x, y


# def NoiseFilter(pos):
#     global cam_list
#     global hCam
#     New = cv2.getTrackbarPos('NoiseFilter', cam_name)
#     # print pos
#     New = True if New else False
#     print 'NoiseFilter:', MVCam1.SetNoiseFilter(hCam, New)

#FOV max value is (1280-640, 960-480)
def createTrackbar_FOV(Width, Height):
    cv2.createTrackbar('VOffsetFOV', cam_name, 0, 1280-Width, FOV)
    cv2.createTrackbar('HOffsetFOV', cam_name, 0, 960-Height, FOV)


if __name__ == '__main__':
    MVCam1 = MVCam()
    if not MVCam1.EnumerateDevice():
        print 'Cannot find any cameras!'
        exit(-1)
    resolution = (1280, 1024)
    cam_list = MVCam1.Getname()
    cam_list = cam_list.split(',')
    print '-------------------------------------------------'
    print 'There are all cameras we Found!'
    for i, name in enumerate(cam_list):
        print "%d "%i + name
    print 'Please input 0~%d to open camera:' % (len(cam_list)-1),
    index = int(raw_input())
    if index not in range(len(cam_list)):
        print "inpur error!!!"
        exit(-1)
    cam_name = cam_list[index]
    window_name = 'MVCam %s' % cam_name
    cv2.namedWindow(cam_name, cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
    hCam = MVCam1.Init(cam_name)
    # hCam1 = MVCam1.Init(cam_list1[0])
    print 'hCam', hCam
    print 'SetImageResolution', MVCam1.SetImageResolution(hCam, resolution[0], resolution[1])
    print 'SetTriggerMode', MVCam1.SetTriggerMode(hCam, 1)
    print 'CameraSetTriggerCount', MVCam1.SetTriggerCount(hCam, 1)
    print 'Play', MVCam1.Play(hCam)

    cv2.createTrackbar('AeState', cam_name, 0, 1, AeState)
    cv2.createTrackbar('AnalogGain', cam_name, 8, 256, AnalogGain)
    cv2.createTrackbar('expose', cam_name, 2000, 100000, expose)
    cv2.createTrackbar('AutoWb', cam_name, 1, 1, AutoWb)
    cv2.createTrackbar('red', cam_name, 100, 399, colorTemp)
    cv2.createTrackbar('green', cam_name, 100, 399, colorTemp)
    cv2.createTrackbar('blue', cam_name, 100, 399, colorTemp)
    cv2.createTrackbar('saturation', cam_name, 100, 255, colorTemp)

    cv2.createTrackbar('gamma', cam_name, 50, 255, gammacontrast)
    cv2.createTrackbar('contrast', cam_name, 100, 255, gammacontrast)
    cv2.createTrackbar('Sharpness', cam_name, 0, 255, Sharpness)
    # cv2.createTrackbar('NoiseFilter', cam_name, 0, 1, NoiseFilter)
    cv2.createTrackbar('Threshold', cam_name, 50, 255, Threshold)
    #createTrackbar_FOV(640, 480)

    #drag will trigger (pos) function
    AeState(0)
    AnalogGain(0)
    expose(0)
    AutoWb(0)
    colorTemp(0)
    gammacontrast(0)
    Sharpness(0)
    # NoiseFilter(0)
    st = time.time()
    print '-------------------------------------------------'
    print 'input 1~4 in to Set resolution\n'\
     + '1: 1280*960   , 2: 1280*720\n'\
     + '3: 960*480    , 4: 640*480 \n'

    #---------------necessary--------------------
    while True:
        img = MVCam1.getImage(hCam, 1000)
        if img is None:
            break
    #---------------necessary--------------------
    i = 0
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    maxValue = 0
    while True:
        MVCam1.SoftTrigger(hCam)
        img0 = MVCam1.getImage(hCam, 1000)
        if img0 is not None:
            # print img0
            ed = time.time()
            delta_time = ed - st

            cv2.setMouseCallback(window_name, getXY)
            print 'x1 = ',x1,'y1 = ',y1,'x2 = ',x2,'y2 = ',y2
            cv2.rectangle(img0,(x1,y1),(x2,y2),0)
            I_ROI = img0[x1:x2,y1:y2]
            S = cv2.Sobel(I_ROI,cv2.CV_16U,1,1,ksize = 3)
            Value = cv2.mean(S)[0]
            print Value
            if Value > maxValue:
                maxValue = Value
            cv2.putText(img0,"current:"+str(Value),(100,100),cv2.FONT_HERSHEY_PLAIN,1,0)
            cv2.putText(img0,"max:"+str(maxValue),(100,150),cv2.FONT_HERSHEY_PLAIN,1,0)

            sys.stdout.write('\r' + str(cam_name) + " fps: " + str(delta_time)+'\n')
            sys.stdout.flush()
            cv2.imshow(window_name, img0)
            
            st = time.time()
        else:
            print '\nImg is None',
        key = chr(cv2.waitKey(5) & 255)
        if key in ['q', 'Q']:
            print '\nUnInit', MVCam1.UnInit(hCam)
            # print 'UnInit', MVCam1.UnInit(hCam1)
            break
        elif key in ['c', 'C']:
            cv2.imwrite("./test.png", img0)
            print "saved image "
        elif key in ['p', 'P']:
            print '\nPlay', MVCam1.Play(hCam)
        elif key in ['r', 'R']:
            maxValue = 0
            print '\nReset'            
        elif key in ['1']:
            print 'SetImageResolution', MVCam1.SetImageResolution(hCam, 1280, 960)
            # createTrackbar_FOV(1280,960)
        elif key in ['2']:
            print 'SetImageResolution', MVCam1.SetImageResolution(hCam, 1280, 720)
            # createTrackbar_FOV(1280,720)
        elif key in ['3']:
            print 'SetImageResolution', MVCam1.SetImageResolution(hCam, 960, 480)
            # createTrackbar_FOV(960,480)
        elif key in ['4']:
            print 'SetImageResolution', MVCam1.SetImageResolution(hCam, 640, 480)
            # createTrackbar_FOV(640,480)



