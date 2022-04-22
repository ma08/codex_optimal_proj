import sys
input = sys.stdin.readline


N = int(input())
H = list(map(int, input().split()))

if N == 1:
    print(1)
    print("R")
else:
    L = [H[0]]
    R = [H[N-1]]
    L_i = 1
    R_i = N-2
    while L_i < R_i:
        if H[L_i] > L[-1]:
            L.append(H[L_i])
            L_i += 1
        if H[R_i] > R[-1]:
            R.append(H[R_i])
            R_i -= 1
        if H[L_i] <= L[-1] and H[R_i] <= R[-1]:
            break
    if len(L) > len(R):
        print(len(L))
        print("L"*len(L))
    else:
        print(len(R))
        print("R"*len(R))
