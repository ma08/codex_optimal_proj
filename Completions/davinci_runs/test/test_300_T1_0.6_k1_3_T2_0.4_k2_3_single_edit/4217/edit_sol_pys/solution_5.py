# https://atcoder.jp/contests/abc087/tasks/abc087_b

# Get input
N, M = map(int, input().split())

# Init
A = []
for i in range(N):
    K = int(input().split()[0])
    A.append(list(map(int, input().split())))

# Main
answer = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i + j + k == 500:
                answer += 1
print(answer)
