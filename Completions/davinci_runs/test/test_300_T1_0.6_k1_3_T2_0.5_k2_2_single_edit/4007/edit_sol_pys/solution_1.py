def solve(n, a, b, c, d):
    if n == 1:
        return "Yes"
    if n == 2:
        if a == c and b == d:
            return "Yes"
        else:
            return "No"
    if a == c and b == d:
        return "Yes"
    if n % 2 == 1:
        return "No"
    if a == c:
        return solve(n / 2, a, b, c, d)
    if b == d:
        return solve(n / 2, a, b, c, d)
    if a == d:
        return solve(n / 2, a, b, c, d)
    if b == c:
        return solve(n / 2, a, b, c, d)
    return "No"



def main():
    n = int(input())
    a, b, c, d = map(int, input().split())
    result = solve(n, a, b, c, d)
    print(result)

if __name__ == "__main__":
    main()
