

from collections import deque
from sys import stdin, stdout
 
n, m, k = map(int, stdin.readline().split())
a = deque(map(int, stdin.readline().split()))
b = deque(map(int, stdin.readline().split()))
 
result = 0
while a and b:
    if a[0] < b[0]:
        a.popleft()
    elif a[0] > b[0]:
        b.popleft()
    else:
        if k == 0:
            b.popleft()
        else:
            a.popleft()
            b.popleft()
            k -= 1
 
        result += 1
 
stdout.write(str(result))
