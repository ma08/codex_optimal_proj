

n = int(input())
a = [int(x) for x in input().split() if int(x) > 0]
a.sort()

for i in range(len(a)):
    if a[i] != i+1:
        print(i+1)
        break
else:
    print(len(a)+1)
