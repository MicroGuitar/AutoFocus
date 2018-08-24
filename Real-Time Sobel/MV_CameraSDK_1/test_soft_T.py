from MVCam_py import MVCam
import cv2
import numpy as np
import sys
import time


if __name__ == "__main__":
	MVCam1 = MVCam()

	MVCam1.EnumerateDevice()

	cv2.namedWindow('img')

	hCam = MVCam1.Init("cam44")
	MVCam1.SetImageResolution(hCam, 1280, 960)
	MVCam1.SetExposureTime(hCam, 10000)

	print 'play', MVCam1.Play(hCam)
	print 'SetTriggerMode', MVCam1.SetTriggerMode(hCam, 1)
	# print 'CameraSetTriggerCount', MVCam1.SetTriggerCount(hCam, 1)
	time.sleep(2)
	t = time.time()
	while True:
		# print 'SetTriggerMode', MVCam1.SetTriggerMode(hCam, 1)
		# time.sleep(0.01)
		print 'SoftTrigger', MVCam1.SoftTrigger(hCam)

		# MVCam1.Play(hCam)
		img0 = MVCam1.getImage(hCam,1000)
		# MVCam1.Stop(hCam)
		print time.time() - t
		t = time.time()
		if img0 != None:
			cv2.imshow('img', img0)
		else:
			print 'img0 is None!!'

		# img1 = MVCam1.getImage(hCam,1000)
		# print time.time() - t
		# if img1 != None:
		# 	cv2.imshow('img1', img1)
		# else:
		# 	print 'img1 is None!!'

		key = chr(cv2.waitKey(5) & 255)
		if key == 'g':
			print 'SoftTrigger', MVCam1.SoftTrigger(hCam)
			# print 'SoftTrigger', MVCam1.SoftTrigger(hCam)
		elif key == 'q':
			print '\nUnInit', MVCam1.UnInit(hCam)
			break
		# print 'SetTriggerMode', MVCam1.SetTriggerMode(hCam, 0)
		# time.sleep(2)

