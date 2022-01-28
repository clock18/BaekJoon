# 크로아티아 알파벳
# Ascii Code : A => 65, a => 97
# a.replact(b,c) => a리스트에 포함된 b문자를 c로 치환하라

croList = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = input('')
for i in range(len(croList)):
    a = a.replace(croList[i], chr(65+i))

print(len(a))