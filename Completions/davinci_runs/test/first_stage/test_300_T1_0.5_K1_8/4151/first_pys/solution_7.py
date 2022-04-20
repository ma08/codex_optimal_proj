

n = int(input())
a = list(map(int, input().split()))

# find the number of distinct elements
distinct = []
for i in a:
    if i not in distinct:
        distinct.append(i)

# find the number of occurences of each distinct element
occurences = []
for i in distinct:
    occurences.append(a.count(i))

# find the number of ways to arrange the occurences
ways = 1
for i in occurences:
    ways = (ways*(i+1)) % 998244353

# print the answer
print(ways)