# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 입력의 마지막에는 0 두 개가 들어온다.

# 각 테스트 케이스마다 A+B를 출력한다.

# 1번째 방법
# while True:
#     inputNum = input('숫자 두개 입력 : ')
#     a, b = map(int, inputNum.split(' '))
#     if a == 0 and b == 0:
#         break
#     else:
#         print(a + b)



# 2번째 방법
num = 0
list_a = []
list_b = []

# 무한반복문을 사용하고 break를 사용하여 반복문 탈출을 한다.
while(1):
    a, b = map(int, input().split())
    #입력된 값이 0 0 일시 반복문 종료
    if a == 0 and b == 0:
        break
    # 입력된 값이 0 0 아닐시 a와 b를 따로 리스트에 저장해준다.
    else:
        list_a.append(a)
        list_b.append(b)
        num = num + 1

# list_a와 list_b의 인덱스 값이 같으면 같은 줄에 입력된 숫자이니 두 수를 더해서 출력해주는 코드
for i in range(0, num):
    print(list_a[i] + list_b[i])

# [출처] 백준 10952번: A+B - 5|작성자 changbro

