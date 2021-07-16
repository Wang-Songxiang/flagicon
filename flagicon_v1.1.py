import numpy as np
import cv2
import sys

fname_in  = sys.argv[1]
fname_out = "out.png"

img_in = cv2.imread( fname_in  )
flag = cv2.imread("flag.png")
img_out = cv2.resize(img_in,(640,640), interpolation=cv2.INTER_AREA)  

rows,cols,channels = flag.shape
roi = img_out[0:rows, 0:cols ]

flaggray = cv2.cvtColor(flag,cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(flaggray, 240, 255, cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask = mask)

img2_fg = cv2.bitwise_and(flag,flag,mask = mask_inv)


dst = cv2.add(img1_bg,img2_fg)
img_out[0:rows, 0:cols ] = dst

cv2.imwrite( fname_out, img_out)