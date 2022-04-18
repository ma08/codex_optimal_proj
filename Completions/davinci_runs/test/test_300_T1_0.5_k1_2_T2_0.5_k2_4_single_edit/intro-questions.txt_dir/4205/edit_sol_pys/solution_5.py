

N = int(input())
sequence = list(map(int, input().split()))
seq = sorted(sequence)
if(sequence == seq):
    print("YES")
else:
    print("NO")
