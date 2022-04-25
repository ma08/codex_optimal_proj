

def solve(n, m, c, b, A):
    count = 0
    for i in range(n):
        if A[i][0] * b[0] + A[i][1] * b[1] + A[i][2] * b[2] + c > 0:
            count += 1
    return count

if __name__ == '__main__':
    n, m, c = map(int, raw_input().split())
    b = map(int, raw_input().split())
    A = []
    for i in range(n):
        A.append(map(int, raw_input().split()))
    print solve(n, m, c, b, A)
