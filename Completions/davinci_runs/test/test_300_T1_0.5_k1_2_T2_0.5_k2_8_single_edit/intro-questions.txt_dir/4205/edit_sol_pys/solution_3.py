

N = int(input())
sequence = list(map(int, input().split()))
flag = True
for i in range(N-1):
    if(sequence[i] > sequence[i+1]):
        flag = False
        break
if(flag):
    print("YES")
else:
    print("NO")
