# 6.
N = int(input('숫자입력 : '))

for i in range(N,0,-1):
    if N <= 100000:
        print(i)
    else:
        print('범위를 초과하였습니다.')