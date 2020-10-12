from PIL import Image
import cv2
import numpy as np
import pytesseract
import time
pytesseract.pytesseract.tesseract_cmd = r'E:\\TesseractOCR\\tesseract.exe'

image = cv2.imread('test12.png')
#image=cv2.resize(image,dsize=(500,500),interpolation=cv2.INTER_AREA) # 리사이즈
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
start = time.time()
print(pytesseract.image_to_string(image, lang='kor'))
end= time.time()
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print("실행시간",(end-start),"초")

#글자 박스 그리기
"""
hImag,wImag,_=image.shape
boxes = pytesseract.image_to_boxes(image,lang='kor')

for b in boxes.splitlines():
    b = b.split(' ')
    #print(b)
    x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(image,(x,hImag-y),(w,hImag-h),(0,0,255),1)

cv2.imshow('Result',image)
cv2.waitKey(0)
"""
"""
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ전처리ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
image = cv2.imread('test6.jpg')
hImag,wImag,_=image.shape
if hImag >2000:
    hImag = int(hImag/4)
if wImag >2000:
    wImag = int(wImag/4)

#gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image=cv2.resize(image,dsize=(hImag,wImag),interpolation=cv2.INTER_AREA)


boxes = pytesseract.image_to_boxes(image,lang='kor')
print(pytesseract.image_to_string(image, lang='kor'))

for b in boxes.splitlines():
    b = b.split(' ')
    print(b)
    x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(image,(x,hImag-y),(w,hImag-h),(0,0,255),1)

cv2.imshow('Result',image)
cv2.waitKey(0)

"""