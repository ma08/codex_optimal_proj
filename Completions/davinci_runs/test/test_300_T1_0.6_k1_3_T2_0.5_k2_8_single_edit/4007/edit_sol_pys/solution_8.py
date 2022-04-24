

def solve(n, a, b):
    return "Yay!" if a <= n <= b else ":("

def main():
    n = int(input())
    friends = list(map(int, input().split()))
    result = solve(n, friends)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
