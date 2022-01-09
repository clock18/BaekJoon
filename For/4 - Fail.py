# 4.
T = int(input('테스트케이스의 개수 : '))

if T <= 1000000:
    for i in range(T):
        A, B = map(int, input().split(' '))
        if 1 <= A <= 1000 and 1 <= B <= 1000:
            print(A + B)
        else:
            print('범위를 초과하였습니다.')
else:
    print('범위를 초과하였습니다')