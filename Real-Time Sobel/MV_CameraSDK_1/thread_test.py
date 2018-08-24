from MVCam_py import MVCam
import cv2
import numpy as np
import sys
import time
import threading

img0 = None



def getimg(MVCam1, hCam):
	global img0
	# MVCam1.Stop(hCam)
	while True:
		time.sleep(1)
		# t0 = time.time()
		print 'SoftTrigger', MVCam1.SoftTrigger(hCam)
		print 'before read: ', time.time() - t0
		img0 = MVCam1.getImage(hCam,1000)
		print 'end read: ', time.time() - t0
		print 'end read: ', time.time() - t0
		print 'end read: ', time.time() - t0
		print 'end read: ', time.time() - t0


if __name__ == "__main__":
	t0 = time.time()

	MVCam1 = MVCam()
	MVCam1.EnumerateDevice()

	hCam = MVCam1.Init("Cam3")
	MVCam1.SetImageResolution(hCam,1280,960)
	MVCam1.SetExposureTime(hCam, 10000)
	print 'SetTriggerMode', MVCam1.SetTriggerMode(hCam, 1)
	print 'play', MVCam1.Play(hCam)

	th = threading.Thread(target=getimg, args=(MVCam1, hCam))

	th.daemon = True
	print 'before st'
	th.start()
	print 'st done'
	st = time.time()
	while True:
		time.sleep(0.01)
		# if img0 != None:
		# 	# cv2.imshow('img', img0)
		# 	print 'img'
		# else:
		# 	print 'img0 is None!!'
		# cv2.waitKey(10)

		# print time.time() - st
		print time.time() - t0
		st = time.time()



