

def main():
    cases = int(input())
    for i in range(cases):
        a, b, n, S = map(int, input().split())
        if S > a * n + b:
            print("NO")
            continue
        if S % n == 0 and S / n <= a:
            print("YES")
            continue
        if S <= b:
            print("YES")
            continue
        print("NO")

main()
