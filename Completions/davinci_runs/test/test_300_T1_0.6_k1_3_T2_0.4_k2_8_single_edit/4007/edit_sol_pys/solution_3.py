
def solve(n, friends):
    for i in range(n):
        if friends[i] == 0:
            for j in range(1, n + 1):
                if j not in friends and j != i + 1 and j != 0:
                    friends[i] = j
                    break

    return friends

def main():
    n = int(input())
    friends = list(map(int, input().split()))
    result = solve(n, friends)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
