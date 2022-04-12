

def main():
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        if k > n:
            print('NO')
            continue
        print('YES')
        for i in range(1, k+1):
            print(i, end=' ')
        print(n)
            
if __name__ == '__main__':
    main()
