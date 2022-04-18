

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    
    if a == [0] * n:
        print(0)
        return
    if b == [0] * n:
        print(n)
        return
    
    a.sort()
    b.sort()
    ans = 0
        if a[i] * b[n - 1 - i] == 0:
            ans += 1
            continue
    for i in range(n):
        if a[i] * b[n - 1 - i] > 0:
            break
    print(ans)

if __name__ == '__main__':
    main()
