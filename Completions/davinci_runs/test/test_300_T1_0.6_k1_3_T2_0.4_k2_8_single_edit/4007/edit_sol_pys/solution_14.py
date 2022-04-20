

def solve(n, s):
    if n % 2 == 0:
        return "No"
    else:
        return "Yes"

def main():
    n = int(input())
    s = list(map(int, input().split()))
    result = solve(n, s)
    print(result)

if __name__ == "__main__":
    main()
