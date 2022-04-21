
n = input()
num = list(map(int, input().strip()))
f = list(map(int, input().strip().split()))
for i in range(len(num)):
    num[i] = f[num[i]-1]
print(''.join(map(str, num)))
