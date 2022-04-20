

def solve(n, a, k):
    max_len = 1
    curr_len = 1
    for i in range(1, n):
        if a[i] - a[i-1] == k:
            curr_len += 1
        else:
            max_len = max(max_len, curr_len)
            curr_len = 1
    return max_len

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))[:n]
    k = int(input())
    print(solve(n, a, k))
