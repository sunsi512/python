# 리스트 = []
# 세트 = set({})
# 튜플 = ()

# 리스트.append(1)
# 리스트.append(2)
# 리스트.append(3)
# print(리스트)

# # set 추가하기 (중복불가)
# 세트.add(1)
# 세트.add(2)
# 세트.add(3)
# # set 제거하기
# 세트.discard
# print(세트)

# 튜플 = tuple(리스트)
# print(튜플)


#67p
여행지 = set({})
a = 0
while a<3:
    q = input('희망하는 수학여행지를 입력하세요 >>>')
    여행지.add(q)
    a += 1
print(여행지)
                                                        