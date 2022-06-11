

# money = int(input('넣을 돈을 입력해주세요 >>>'))
# can = 0
# while money > 700:
#     print('음료수 = {}개, 잔돈 = {}원'.format(can, money))
#     can += 1
#     money -= 700
# print('음료수 = {}개, 잔돈 = {}원'.format(can, money))


def 절댓값더하기(숫자1, 숫자2):
    if 숫자1 < 0:
        숫자1 *= -1
        if 숫자2 < 0:
            숫자2*= -1
        return 숫자1 + 숫자2
    elif 숫자2 < 0:
        숫자2 *= -1
        return 숫자1 + 숫자2
    else:
        return 숫자1 + 숫자2
print(절댓값더하기(3, -1))
print(절댓값더하기(5, 2))
print(절댓값더하기(-3, -2))