# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 첫째 줄에 A/B를 출력한다.
# 실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답이다.

a = input('숫자 두개 입력 : ')
b, c = map(int,a.split())
print(b / c)