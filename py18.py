#나이 = 11
#if 나이 >= 20:
   # print('성인')
#else:
   # print('미성년자')

#95p
# 나이에 따라서 프로그램의 동작을 다르게 if~elif~else
age = int(input('몇 살입니까? >>>'))
if age >= 20:
    print('성인')
elif age >= 0:
    print('미성년자')
else:
    print('?')