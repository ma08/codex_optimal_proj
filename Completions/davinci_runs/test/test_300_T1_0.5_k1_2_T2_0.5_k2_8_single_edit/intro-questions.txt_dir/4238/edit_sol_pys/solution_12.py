from collections import Counter




n = int(input())
a = list(map(int,input().split()))
c = Counter(a)
print(c)
