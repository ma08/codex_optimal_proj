

def solve(n, a, b):
    max_len = 1
    curr_len = 1
    for i in range(1, n):
        if b[i] > b[i-1]:
            curr_len += 1
        else:
            max_len = max(max_len, curr_len)
            curr_len = 1
    return max(max_len, curr_len)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:n]
    print(solve(n, a, b))
