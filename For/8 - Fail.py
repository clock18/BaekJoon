# 8.
T = int(input('테스트 케이스 입력 : '))

for i in range(1,T+1):
    a, b = map(int, input().split(' '))
    if 0 < a < 10 and 0 < b < 10:
        sum = a + b
        print(f'Case #{i}: {a} + {b} = {sum}')
    else:
        print('범위를 초과하였습니다.')
