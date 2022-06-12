import cv2
import mediapipe as mp

# 이미지에서 얼굴찾기
cap = cv2.VideoCapture('zxcv.mp4')

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.60)       #60% 이상 얼굴로 인식될경우

while True:
    success, img = cap.read()
    if success:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = faceDetection.process(imgRGB)
        if results.detections:             # 찾았으면
            print('찾음')
            for id, detection in enumerate(results.detections):
                mpDraw.draw_detection(img,detection)          #얼굴 위치에 네모표시
        cv2.imshow('Inage', img)
        if cv2.waitKey(20) & 0xFF == 27:
            break