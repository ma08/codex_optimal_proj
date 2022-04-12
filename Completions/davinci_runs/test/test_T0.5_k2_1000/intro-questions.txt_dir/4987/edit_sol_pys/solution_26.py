# 옷의 종류 수
# 옷을 최대 몇 개까지 같이 세트로 팔 수 있는지
# 옷의 세트를 팔 때 옷의 색깔이 같은 옷은 최대 몇 개까지 팔 수 있는지
from sys import stdin

S, C, K = map(int, stdin.readline().split())
D = list(map(int, stdin.readline().split()))

D.sort()

machine_count = 0

for i in range(0, S, C):
    machine_count += 1

    if K == 0:
        continue

    for j in range(i, i + C - 1):
        if abs(D[j] - D[j + 1]) > K:
            machine_count += 1
            break

print(machine_count)
