
def solve(n, friends):
    pass

def main():
    n = int(input())
    friends = list(map(int, input().split()))
    result = solve(n, friends)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
