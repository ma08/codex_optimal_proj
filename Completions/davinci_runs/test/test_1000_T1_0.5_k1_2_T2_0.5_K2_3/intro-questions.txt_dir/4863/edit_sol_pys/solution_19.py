

n = int(input())
s = 0 
for i in range(1, n+1):
    answer = input().strip()
    if answer == 'A' or answer == 'a':
        s += 1
print(s)
