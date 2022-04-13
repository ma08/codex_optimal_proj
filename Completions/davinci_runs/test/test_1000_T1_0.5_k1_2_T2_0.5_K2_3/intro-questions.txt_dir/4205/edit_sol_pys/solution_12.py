
N = int(input())
sequence = list(map(int, input().split()))

if sequence == sorted(sequence):
    print("yes")
else:
    print("no")
