# 3.
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
# 1부터 n까지 합을 출력한다.

a = int(input('숫자 입력 : '))
b = 0

if a>=1 and a<=10000:
    for i in range(1, a + 1):
        b += i

    print(b)