# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가,
# 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

# 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

a = int(input('숫자 1 입력 : '))
b = input('숫자 2 입력 : ')

print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))



