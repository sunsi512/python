from time import sleep

from cv2 import convertPointsToHomogeneous
i = 0
while True:
    #sleep(1)
    print('무한반복')
    i += 1
    if i >= 5:
        break           #break가 실행되면 반복문이 즉시 종료

for i in range(1, 11):
        if i % 2 == 0:
            continue
        print(i)


#예제 1)
num = 0
while True:
    num += 1
    if(num > 5):
        break
    print(num)

#예제 2)
for num in range(10):
    if (num%2) == 1:
        continue
    print(num)