import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

def hangulText(image, text, pos, size, color):
    img_pil = Image.fromarray(image)        # 이미지를 np리스트형태로 만든다
    img_draw = ImageDraw.Draw(img_pil)      # 그림을 그릴 공간 지정
    font = ImageFont.truetype('H2PORM.TTF', size)    # 폰트와 사이즈 설정
    img_draw.text(pos, text, font=font, fill=color)  # 글자 그리기
    return np.array(img_pil)

width = 198-57
height = 123-17
origin_pos = np.array([[57, 17],[198, 17],[57, 123],[198, 123]], dtype=np.float32)
change_pos = np.array([[0,0],[width, 0],[0,height],[width, height]], dtype = np.float32)
matrix = cv2.getPerspectiveTransform(origin_pos, change_pos)

img = cv2.imread('asdf2.jpg')       # 이미지 읽기
img_change = cv2.warpPerspective(img, matrix, (width, height))

img_change = hangulText(img_change, '강시연', (10, 10), 10, (255, 0, 255))

cv2.imshow('my titile', img)        # 원본 이미지 보여주기
cv2.imshow('change image', img_change)
cv2.waitKey(0)                      # 무한대기


#21, 2   /  247, 2
#21, 178 /  247, 178