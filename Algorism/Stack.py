# π‘ sys.stdin.readline() μ¬μ©λ²
# πν κ°μ μ μλ₯Ό μλ ₯λ°μ λ
# import sys
# a = int(sys.stdin.readline())
# π¨ κ·Έλ₯ a = sys.stdin.readline() νλ©΄ μλλμ?
# π sys.stdin.readline()μ νμ€ λ¨μλ‘ μλ ₯λ°κΈ° λλ¬Έμ, κ°νλ¬Έμκ° κ°μ΄ μλ ₯ λ°μμ§λλ€.
# λ§μ½ 3μ μλ ₯νλ€λ©΄, 3\n μ΄ μ μ₯λκΈ° λλ¬Έμ, κ°νλ¬Έμλ₯Ό μ κ±°ν΄μΌ ν©λλ€.
# λν, λ³μ νμμ΄ λ¬Έμμ΄ νν(str)λ‘ μ μ₯λκΈ° λλ¬Έμ,
# μ μλ‘ μ¬μ©νκΈ° μν΄μ νλ³νμ κ±°μ³μΌ ν©λλ€.
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