import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    T = []
    A = []
    for i in range(N):
        t,a = map(int, sys.stdin.readline().rstrip().split())
        T.append(t)
        A.append(a)
    #print(T,A) 
    ans = 1
    for i in range(N):
        if i == 0:
            ans = T[0] + A[0] - 1
        else:
            ans = T[i] + A[i] - 1
            if ans % T[i] != 0:
                ans += T[i] - ans % T[i]
            if ans % A[i] != 0:
                ans += A[i] - ans % A[i]
    print(ans)

if __name__ == '__main__':
    main()
