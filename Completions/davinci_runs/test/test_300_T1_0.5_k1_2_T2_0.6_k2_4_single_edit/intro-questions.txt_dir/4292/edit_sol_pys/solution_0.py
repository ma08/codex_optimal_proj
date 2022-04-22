

import sys

n, k = map(int, sys.stdin.readline().split()) # n: 가지고 있는 동전의 수, k: 상근이가 만들어야 하는 최대가격
p = list(map(int, sys.stdin.readline().split())) # p: 상근이가 가지고 있는 동전의 종류

print(sum(sorted(p)[:k])) # 상근이가 만들어야 하는 최대 가격을 만들 수 있는 동전 중 가장 작은 동전의 가격을 모두 더한다
