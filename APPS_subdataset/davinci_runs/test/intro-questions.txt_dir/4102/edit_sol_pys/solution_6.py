
n = input().split()

if int(n[0]) + int(n[1]) == int(n[2]) or int(n[1]) + int(n[2]) == int(n[0]) or int(n[0]) + int(n[2]) == int(n[1]):
    print("Yes")
else:
    print("No")
