from collections import Counter


n = int(input())  # number of elements
a = list(map(int, input().split()))  # elements

c = Counter(a)

for i in range(1, n + 1):
    if i not in c:
        print(i)
        break

