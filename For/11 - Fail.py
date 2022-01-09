# 11.
# 1)

# a = input('정수 두 개 입력 : ')
# b = input('수열 입력 : ')
#
# a = a.split()
# b = b.split()
#
# for i in b:
#     if int(a[1]) > int(i):
#         print(i, end=' ')


# 2)

N, X = map(int, input('두 정수 입력 : ').split())
pro = list(map(int,input('수열 입력 : ').split()))

for i in range(len(pro)):
    if pro[i] < X:
        print(pro[i], end=' ')