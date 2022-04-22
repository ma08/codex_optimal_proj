
def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    
    if A == [0] * n:
        print(0)
        return
    if B == [0] * n:
        print(n)
        return
    
    A.sort()
    B.sort()
    ans = 0
    for i in range(n):
        if A[i] * B[n - 1 - i] > 0:
            break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
