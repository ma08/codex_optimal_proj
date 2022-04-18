

N = int(input())

def is_shichigosan(n):
    if '7' not in n or '5' not in n or '3' not in n:
        return False

count = 0
for i in range(1, N+1):
    if is_shichigosan(str(i)):
        count += 1

print(count)
