from PIL import Image
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'E:\TesseractOCR\tesseract'


print(pytesseract.image_to_string(Image.open('test2.jpg'), lang='kor'))
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ전처리ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
image = cv2.imread('test2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#gray = cv2.medianBlur(gray, 10)
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img_rgb, lang='kor'))
