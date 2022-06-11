import cv2

def 이미지띄우기():
    img = cv2.imread('ing1.png')
    cv2.imshow('title', img)
    cv2.waitKey(0)

 
def 이미지띄우기2(이미지이름):
    img = cv2.imread(이미지이름)
    cv2.imshow('title', img)
    cv2.waitKey(0)

def 회색이미지(이미지):
    img = cv2.imread(이미지)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('title', gray)
    cv2.waitKey(0)

# #함수사용
# # 이미지띄우기2('ing1.png')
# # 이미지띄우기2('asdf.jpg')
# 회색이미지('asdf.jpg')