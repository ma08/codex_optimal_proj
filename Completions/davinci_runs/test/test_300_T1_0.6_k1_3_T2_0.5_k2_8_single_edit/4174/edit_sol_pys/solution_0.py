
def main():
    n = int(input())
    a, b = map(int, input().split())
    k = int(input())
    p = list(map(int, input().split()))
    s = set(p)
    if len(s) == k and a not in s and b not in s:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
