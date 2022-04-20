

n = int(input())
a = input().split()

for i in range(n):
    if int(a[i]) % 2 == 0 and (int(a[i]) % 3 != 0 and int(a[i]) % 5 != 0):
        print("DENIED")
        break
    elif i == n-1:
        print("APPROVED")