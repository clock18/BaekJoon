num = int(input())
line = 0
max = 0

while max < num:
    line += 1
    max += line

dif = max - num
if line % 2 == 0:
    top = line - dif
    down = dif + 1
else:
    top = dif + 1
    down = line - dif

print(f'{top}/{down}')



