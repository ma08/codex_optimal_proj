
n = int(input())
for i in range(n):
    if len(input()) == len(set(input())):
        print("Yes")
    else:
        print("No")
