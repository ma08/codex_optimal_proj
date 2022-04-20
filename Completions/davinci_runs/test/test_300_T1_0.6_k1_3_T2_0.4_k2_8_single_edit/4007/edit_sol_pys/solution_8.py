

def solve(n, friends):
    for i in range(n - 1):
        if friends[i] == 0 and friends[i + 1] == 0:
            friends[i] = i + 1
            friends[i + 1] = i + 2
        elif friends[i] == 0 and friends[i + 1] != 0:
            friends[i] = friends[i + 1] - 1
        elif friends[i] != 0 and friends[i + 1] == 0:
            friends[i + 1] = friends[i] + 1
    return friends

def main():
    n = int(input())
    friends = list(map(int, input().split()))
    result = solve(n, friends)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
