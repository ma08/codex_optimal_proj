
N = int(input())
for i in range(N):
    sequence = list(map(int, input().split()))
    if(sequence == sorted(sequence)):
        print("YES")
    else:
        print("NO")
