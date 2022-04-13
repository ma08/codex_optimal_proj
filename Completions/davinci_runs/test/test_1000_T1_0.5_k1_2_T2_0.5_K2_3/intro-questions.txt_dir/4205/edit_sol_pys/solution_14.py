

N = int(input())
sequence = list(map(int, input().split()))[:N]

if(sequence == sorted(sequence)):
    print("YES")
else:
    print("NO")
