

#input
K = int(input())
A, B = map(int(input().split()))

#initialize
answer = "NG"

#find range
for i in range(A, B+1):
    if i % K == 0:
        answer = "OK"
        break

#output
print(answer)