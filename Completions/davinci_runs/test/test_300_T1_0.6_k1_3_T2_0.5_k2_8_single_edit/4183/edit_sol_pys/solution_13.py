
from math import gcd
import sys

n = int(input())
t = []
for i in range(n):
    t.append(int(input()))

ans = t[0] #set first element as first answer

for i in t: #for all elements in t
    ans = ans * i // gcd(ans, i) #find the gcd and set it as answer

print(ans)
