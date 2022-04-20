#coding:utf-8

N = int(input())

def is_shichigosan(num):
    if '7' in num and '5' in num and '3' in num:
        return True
    return False

count = 0
for i in range(1, N+1):
    if is_shichigosan(str(i)):
        count += 1

print(count)
