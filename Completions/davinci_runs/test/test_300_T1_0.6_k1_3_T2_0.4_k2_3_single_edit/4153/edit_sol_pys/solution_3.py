from collections import deque

n = int(input())
s = deque(input().split())

count = 0
while s:
    if s[0] == '0':
        count += 1
        s.popleft()
    elif s[0] == '1':
        if len(s) > 1 and s[1] == '0':
            count += 1
            s.popleft()
            s.popleft()
        else:
            break

print(count)
