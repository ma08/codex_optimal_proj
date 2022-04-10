
#------------------------------------------------------------------------------#

def solve(n, k, x, a):
    if x < k:
        return -1
    if x == n:
        return sum(a)

    sum_a = [0] * n
    sum_a[0] = a[0]
    for i in range(1, n):
        sum_a[i] = sum_a[i-1] + a[i]

    max_sum = -1
    for i in range(n):
        if i + k - 1 >= n:
            break
        for j in range(i + k - 1, n):
            if j - i + 1 - x >= 0:
                break
            sum_i = sum_a[i+k-1]
            sum_j = sum_a[j]
            if i > 0:
                sum_i -= sum_a[i-1]
            if j - i + 1 - x > 0:
                sum_j -= sum_a[j - x]
            if max_sum < sum_i + sum_j:
                max_sum = sum_i + sum_j

    return max_sum

#------------------------------------------------------------------------------#

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, x, a))

if __name__ == "__main__":
    main()