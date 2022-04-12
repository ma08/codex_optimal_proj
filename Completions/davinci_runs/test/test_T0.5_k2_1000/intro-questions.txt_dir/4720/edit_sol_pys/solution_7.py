
N = int(input())
seats = [0] * 100001 # seats[i] : i번 좌석의 사람 수

for _ in range(N):
    l, r = map(int, input().split()) # l번 좌석부터 r번 좌석까지 사람이 앉음
    for i in range(l, r+1):
        seats[i] += 1

print(sum(seats))
