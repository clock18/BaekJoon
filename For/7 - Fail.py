# 7.
testCase = int(input('테스트케이스 개수 입력 : '))

for i in range(1,testCase+1):
    a, b = map(int, input().split(' '))
    if 0< a <10 and 0< b < 10:
        sum = a + b
        print(f'Case #{i}: {sum}')
    else:
        print('범위를 초과하였습니다.')