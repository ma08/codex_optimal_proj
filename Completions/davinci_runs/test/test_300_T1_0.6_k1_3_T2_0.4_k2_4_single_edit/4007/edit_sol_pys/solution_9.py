

def solve(n, friends):
    return [i + 1 if friends[i] == 0 else friends[i] for i in range(n)]

def main():
    n = int(input())
    friends = list(map(int, input().split()))
    result = solve(n, friends)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
