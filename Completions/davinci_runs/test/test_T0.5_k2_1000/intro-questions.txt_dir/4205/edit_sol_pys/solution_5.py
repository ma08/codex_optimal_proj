
n = int(input())
sequence = list(map(int, input().split()))[:n]

if sequence == sorted(sequence):
    print("YES")
else:
    print("NO")
