import sys
num = int(sys.stdin.readline())

queue = []
for _ in range(num):
    queueSplit = sys.stdin.readline().split()

    if queueSplit[0] == "push":
        queue.insert(0, queueSplit[1])

    elif queueSplit[0] == "pop":
        if len(queue) != 0:
            print(queue.pop())
        else:
            print(-1)

    elif queueSplit[0] == "size":
        print(len(queue))

    elif queueSplit[0] == "empty":
        if len(queue) == 0:
            print(1)
        else :
            print(0)

    elif queueSplit[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue) - 1])

    elif queueSplit[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])