

#


n = int(input())

for i in range(n):
    total = int(input())
    p = list(map(int, input().split()))
    for j in range(len(p)):
        print(j+1, end=" ")
    print()
