test = int(input())

for _ in range(test):
    h,w,n = map(int, input().split())
    floor = n % h
    num = n // h + 1
    if floor == 0:
        floor = h
        num -= 1
    print(floor*100 + num)
