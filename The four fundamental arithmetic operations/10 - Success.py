# 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C,
# 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

a = input('숫자 3개 입력 : ')
b, c, d = map(int,a.split())

print((b+c)%d)
print(((b%d)+(c%d))%d)
print((b*c)%d)
print(((b%d)*(c%d))%d)