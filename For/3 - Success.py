# 3.
a = int(input('숫자 입력 : '))
b = 0

if a>=1 and a<=10000:
    for i in range(1, a + 1):
        b += i

    print(b)