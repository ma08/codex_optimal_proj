
n = int(input())
d = list(map(int, input().split()))

people = [0] * n
for i in range(1, n):
    people[d[i-1]] = i

print(*people)
