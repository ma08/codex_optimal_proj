

def solve(n, friends):
    for i in range(1, n + 1):
        if i not in friends:
            friends[0] = i
            break
    return friends

def main():
    n = int(input())
    friends = list(map(int, input().split()))
    result = solve(n, friends)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
