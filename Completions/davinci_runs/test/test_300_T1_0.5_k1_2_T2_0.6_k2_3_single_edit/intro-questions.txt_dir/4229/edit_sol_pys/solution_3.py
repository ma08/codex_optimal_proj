

T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    for j in range(N-1):
        for k in range(j+1, N):
            if A[j] == A[k]:
                print("YES")
                print(j+1, k+1)
                break
        else:
            continue
        break
    else:
        print("NO")
