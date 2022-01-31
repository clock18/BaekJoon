n = int(input())

move = 6
hive = 1
first = 1

if n == 1:
    print(1)
else:
    while True:
        first += move
        hive += 1
        if n <= first:
            print(hive)
            break
        move += 6
