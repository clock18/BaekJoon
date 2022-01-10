# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B,
# 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를
# 출력하는 프로그램을 작성하시오.

# 첫째 줄에 시험 점수가 주어진다.
# 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 시험 성적을 출력한다.

num_input = int(input('시험 성적 입력 : '))

if num_input >= 90 and num_input <=100:
    print('A')
elif num_input >= 80 and num_input <= 89:
    print('B')
elif num_input >= 70 and num_input <= 79:
    print('C')
elif num_input >= 60 and num_input <= 69:
    print('D')
elif num_input >= 0 and num_input<= 59:
    print('F')
else:
    print('잘못입력하셨습니다.')