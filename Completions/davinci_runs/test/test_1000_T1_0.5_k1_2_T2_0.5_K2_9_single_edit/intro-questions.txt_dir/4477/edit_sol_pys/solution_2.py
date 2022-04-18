
import collections
 
n = int(input())
 
a = list(map(int, input().split()))
 
a_count = collections.Counter(a)
 
ans = 0
 
for i in a_count:
    if a_count[i] % 2 == 1:
        ans += 1
 
print(ans)
