

def main():
    cases = int(input())
    for i in range(cases):
        a, b, n, s = map(int, input().split())
        if s > a * n + b:
            print("NO")
            continue
        if s % n == 0 and s / n <= a:
            print("YES")
            continue
        if s <= b:
            print("YES")
            continue
        print("NO")

main()
