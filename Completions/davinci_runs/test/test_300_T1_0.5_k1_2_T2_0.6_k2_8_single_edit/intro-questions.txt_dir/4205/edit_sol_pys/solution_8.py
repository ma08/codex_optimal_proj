
N = int(input())
sequence = list(map(int, input().split()))

if(sequence == sorted(sequence)):
elif(sequence == sorted(sequence, reverse=True)):
    print("YES")
    print("YES")
else:
    print("NO")
