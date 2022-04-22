

n, x, y = map(int, input().split())  # n: num of digits, x: position of 1st 0, y: position of 1st 1
n = list(input())  # List of binary digits

for i in range(y, x, -1):
    if n[i] == '0':
        n[i] = '1'
        break
    else:
        n[i] = '0'

print(n.count('0'))
