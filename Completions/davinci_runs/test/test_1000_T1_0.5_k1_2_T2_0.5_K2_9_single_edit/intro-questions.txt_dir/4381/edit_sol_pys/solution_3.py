

n = int(input())
a = list(map(int, input().split()))
print(sum(a) - sum(set(a)))
