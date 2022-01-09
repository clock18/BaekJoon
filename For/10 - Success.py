10.
starNum = int(input('별의 개수 입력 : '))

for i in range(1,starNum+1):
    print(' '*(starNum-i),'*'*i)