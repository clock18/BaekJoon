# 💡 sys.stdin.readline() 사용법
# 📌한 개의 정수를 입력받을 때
# import sys
# a = int(sys.stdin.readline())
# 😨 그냥 a = sys.stdin.readline() 하면 안되나요?
# 👉 sys.stdin.readline()은 한줄 단위로 입력받기 때문에, 개행문자가 같이 입력 받아집니다.
# 만약 3을 입력했다면, 3\n 이 저장되기 때문에, 개행문자를 제거해야 합니다.
# 또한, 변수 타입이 문자열 형태(str)로 저장되기 때문에,
# 정수로 사용하기 위해서 형변환을 거쳐야 합니다.
# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline

import sys
num = int(sys.stdin.readline())

stack=[]
for i in range(num):
    stackSplit = sys.stdin.readline().split()

    if stackSplit[0] == 'push':
        stack.append(stackSplit[1])

    elif stackSplit[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif stackSplit[0] == 'size':
        print(len(stack))

    elif stackSplit[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif stackSplit[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])