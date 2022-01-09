# 5.
N = int(input('입력 숫자 : '))

for i in range(1, N+1):
    if N <= 100000:
        print(i)
    else:
        print('범위를 초과하였습니다.')