

n = int(input())
s = list(map(int, input().split()))

# sort sticks by length
s.sort()

# find the shortest stick
shortest = s[0]
for i in range(n):
    if s[i] < shortest:
        shortest = s[i]

# print the number of sticks that are longer than the shortest stick
print(len([x for x in s if x > shortest]))
