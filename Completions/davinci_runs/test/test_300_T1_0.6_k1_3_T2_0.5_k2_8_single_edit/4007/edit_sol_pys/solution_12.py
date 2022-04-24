

def solve(n, a):
    count = 0
    for i in range(n - 1):
        if a[i] == 0:
            count += 1
            a[i + 1] = 0
    return count

def main():
    n = int(input())
    friends = list(map(int, input().split()))
    result = solve(n, friends)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
