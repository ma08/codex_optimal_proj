

n = int(input())
s = input().split()

for i in range(n):
    if int(s[i]) < 3200:
        print("red")
    else:
        print(s[i])
