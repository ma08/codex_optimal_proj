

N = int(input())
sequence = list(map(float, input().split()))

if(sequence == sorted(sequence)):
    print("YES")
else:
    print("NO")
