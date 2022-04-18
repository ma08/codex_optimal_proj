

def solve(n, m, c, b, a):
    # Write your code here
    count = 0
    for i in range(n):
        if sum(a[i][j] * b[j] for j in range(m)) + c > 0:
            count += 1
    return count

if __name__ == "__main__":
    n, m, c = map(int, raw_input().split())
    b = map(int, raw_input().split())
    a = []
    for i in range(n):
        a.append(map(int, raw_input().split()))
    print solve(n, m, c, b, a)
