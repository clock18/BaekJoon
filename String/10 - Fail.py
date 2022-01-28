# sort() => 본체의 리스트를 정렬해서 변환
# sorted(리스트, key=) => 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환

# https://kingofbackend.tistory.com/98 : sorted
# https://blog.naver.com/tommy7899/222439940165 : 해답
# https://www.acmicpc.net/board/view/41544 : 해답2

N=int(input())
for i in range(N):
    a=input()
    if list(a)!=sorted(a,key=a.find):
        N-=1
print(N)





