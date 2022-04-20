

def solver(n, a):
    max_height = a[0]
    height = a[0]
    for i in range(1, n):
        if a[i] > height:
            return "NO"
        height = max(max_height, a[i])
    return "YES"


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(solver(n, a))
