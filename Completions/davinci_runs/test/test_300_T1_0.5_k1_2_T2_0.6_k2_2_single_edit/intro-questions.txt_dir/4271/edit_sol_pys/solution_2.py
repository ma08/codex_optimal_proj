import sys
input = sys.stdin.readline


n = int(input())  # 공연장 크기
m = int(input())  # 사람 수
k = int(input())  # 좌석 수

# 빈자리를 찾아서 넣는다.
# 연속으로 몇 자리 비워야 하는지 계산해야 한다.

seat = [0] * n
for i in range(m):
    seat[int(input()) - 1] = 1

ans = 0
start = 0
end = 0

while end < n:
    if seat[end] == 0:
        end += 1
    else:
        length = end - start
        if length > k:
            ans += length - k
        end += 1
        start = end

length = end - start
if length > k:
    ans += length - k

print(ans)
