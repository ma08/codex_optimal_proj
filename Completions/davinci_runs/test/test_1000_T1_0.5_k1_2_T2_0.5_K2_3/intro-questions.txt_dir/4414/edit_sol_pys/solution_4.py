

def main():
    cases = int(input())
    for i in range(cases):
        a, b, n, s = map(int, input().split())
        if (s % n == 0 and s / n <= a) or s <= b:
            print('YES')
        else:
            print('NO')

main()
