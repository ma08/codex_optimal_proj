

N = int(input())
sequence = list(map(int, input().split()))

if(sequence == sorted(sequence) and len(sequence) == len(set(sequence))):
    print("YES")
else:
    print("NO")
