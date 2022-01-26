dialList = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input().lower()
cnt = 0

for b in a:
    for i in range(len(dialList)):
        if b in dialList[i]:
            cnt += i + 3

print(cnt)



