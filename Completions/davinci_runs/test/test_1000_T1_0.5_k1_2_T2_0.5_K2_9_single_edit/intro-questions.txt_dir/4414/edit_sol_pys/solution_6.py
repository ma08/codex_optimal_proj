

def main():
    cases = int(input())
    for i in range(cases):
        a, b, n, S = map(int, input().split())
        if S <= a * n + b and (S % n == 0 and S / n <= a or S <= b):
            print("YES")
            continue
        print("NO")

main()
