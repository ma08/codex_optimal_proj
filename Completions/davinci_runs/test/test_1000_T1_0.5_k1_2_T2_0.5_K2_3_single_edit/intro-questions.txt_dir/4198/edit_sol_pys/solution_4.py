

n = int(input())
l = list(map(int, input().split()))

print(sum(l) - max(l) // 2)
