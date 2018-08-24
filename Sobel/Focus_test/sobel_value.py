import cv2
import numpy as np
from matplotlib import pyplot as plt


def getFocusValue(path, x1, x2, y1, y2):
    I = cv2.imread(path, 0)
    I_ROI = I[x1:x2, y1:y2]
    S = cv2.Sobel(I_ROI, cv2.CV_16U, 1, 1, ksize=3)
    Value = cv2.mean(S)[0]
    return Value


    
# Images = []
# for i in range(0, 11):
#     path = 'Src_'+str(i)+'.png'
#     I = cv2.imread(path, 0)
#     I_t = I[300:900, 300:900]
#     S = cv2.Sobel(I_t, cv2.CV_16U, 1, 1, ksize=3)
#     T = cv2.mean(S)[0]
#     Images.append(T)
#
# Images = np.array(Images)
# x = np.arange(0, 11)
# y = Images
#
# fig = plt.figure('new')
# plt.plot(x, y)
# plt.show()
