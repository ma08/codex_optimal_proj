import sys

N = int(input())
items = [input() for _ in range(N)]

result = len(set(items))

print(result)
