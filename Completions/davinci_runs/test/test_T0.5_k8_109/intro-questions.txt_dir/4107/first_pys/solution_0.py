

n, k = map(int, input().split())
s = input()

s = list(s)

cost = 0
for i in range(n):
    if s[i] == '1':
        cost += i+1
        j = i
        while j-k >= 0:
            j -= k
            s[j] = '1'
        j = i
        while j+k < n:
            j += k
            s[j] = '1'

for i in range(n):
    if s[i] == '0':
        cost += i+1

print(cost)