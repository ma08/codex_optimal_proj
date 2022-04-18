

    a = list(map(int, a.split()))
def solver(n, a):
    height = a[0]
    for i in range(1, n):
        if a[i] > height:
            return "NO"
        height = max(height, a[i])
    return "YES"


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(solver(n, a))
