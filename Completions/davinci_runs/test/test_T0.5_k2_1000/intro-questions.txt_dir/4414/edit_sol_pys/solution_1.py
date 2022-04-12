

def main():
    cases = int(input())
    for i in range(cases):
        a, b, n, S = map(int, input().split())
        if S > a * n + b:  # if S is greater than the maximum possible value of S, then S can't be achieved
            print("NO")
            continue
        if S % n == 0 and S / n <= a:  # if S is divisible by n and S/n is less than or equal to a, then S can be achieved
            print("YES")
            continue
        if S <= b:  # if S is less than or equal to b, then S can be achieved
            print("YES")
            continue
        print("NO")

main()
