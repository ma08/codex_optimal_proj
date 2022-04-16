

n = int(input())

for i in range(n):
    arr = [int(x) for x in input().split()]
    if arr[0] == 1:
        print(arr[1])
    else:
        print(arr[1] + arr[2])

a1,b1,a2,b2 = [int(x) for x in input().split()]
c1,d1,c2,d2 = [int(x) for x in input().split()]

g = 0
e = 0

for i in range(a1, b1+1):
    for j in range(a2, b2+1):
        if i+j > c1+d1+c2+d2:
            g += 1
        elif i+j < c1+d1+c2+d2:
            e += 1

if g > e:
    print("Gunnar")
elif g < e:
    print("Emma")
else:
    print("Tie")
