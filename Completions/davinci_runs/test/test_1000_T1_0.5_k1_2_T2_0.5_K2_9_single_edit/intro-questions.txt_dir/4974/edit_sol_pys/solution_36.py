

n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
b = [int(x) for x in input().split()]
for i in b:
    if i in a:
        print("YES")
    else:
        print("NO")
