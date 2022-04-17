

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                a[i] += 1
                a[j] += 1
    if len(set(a)) == 1 and len(set(a)) == n:
        print('YES')
    print('NO')

if __name__ == '__main__':
    main()
