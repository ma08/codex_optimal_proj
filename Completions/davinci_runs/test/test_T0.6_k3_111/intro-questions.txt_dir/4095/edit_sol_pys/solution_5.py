
def solve(n, m, p):
    """
    count number of pairs of indices (l, r) (1 <= l <= r <= n) where the median of p_l, p_{l+1}, ..., p_r is exactly the given number m
    """
    # count the number of elements < m, the number of elements == m, the number of elements > m
    left, mid, right = 0, 0, 0
    # record the number of elements < m in p[:i], the number of elements == m in p[:i], the number of elements > m in p[:i]
    left_count, mid_count, right_count = 0, 0, 0
    for i in range(n):
        if p[i] < m:
            left += 1
            left_count += 1
        elif p[i] > m:
            right += 1
            right_count += 1
        else:
            mid += 1
            mid_count += 1
    # record the number of elements < m in p[i:], the number of elements == m in p[i:], the number of elements > m in p[i:]
    left_count_r, mid_count_r, right_count_r = left, mid, right
    # record the number of combinations of pairs of indices (l, r) (1 <= l <= r <= n) where the median of p_l, p_{l+1}, ..., p_r is exactly the given number m
    count = 0
    # loop through each index i
    for i in range(n):
        # if p[i] == m, then for each index j >= i, we have a pair of indices (i, j) where the median of p_i, p_{i+1}, ..., p_j is exactly the given number m
        if p[i] == m:
            count += n - i
        # if p[i] < m, then we need to find the number of elements > m after p[i]
        elif p[i] < m:
            # if there exists at least one element > m after p[i]
            if right_count_r > 0:
                # we need to find the number of elements > m after p[i] such that the number of elements < m before p[i] is exactly the number of elements > m after p[i]
                # the number of ways to choose the number of elements > m after p[i] from the number of elements > m after p[i] is C(right_count_r, right_count_r - left_count_r)
                # for each of the chosen number of elements > m after p[i], we can choose the positions of these elements from the number of elements > m after p[i] in n - i - 1 ways
                # the number of ways to choose the positions of the number of elements > m after p[i] from the number of elements > m after p[i] is (n - i - 1)^{right_count_r - left_count_r}
                count += nCr(right_count_r, right_count_r - left_count_r) * (n - i - 1) ** (right_count_r - left_count_r)
            # if there exists at least one element == m after p[i]
            if mid_count_r > 0:
                # we need to find the number of elements == m after p[i]
                # for each number of elements == m after p[i] from 1 to mid_count_r, we can choose the positions of these elements from the number of elements == m after p[i] in n - i - 1 ways
                # the number of ways to choose the positions of the number of elements == m after p[i] from the number of elements == m after p[i] is (n - i - 1)^{mid_count_r}
                count += sum(nCr(mid_count_r, i) * (n - i - 1) ** i for i in range(1, mid_count_r + 1))
        # if p[i] > m, then we need to find the number of elements < m before p[i]
        else:
            # if there exists at least one element < m before p[i]
            if left_count > 0:
                # we need to find the number of elements < m before p[i] such that the number of elements > m after p[i] is exactly the number of elements < m before p[i]
                # the number of ways to choose the number of elements < m before p[i] from the number of elements < m before p[i] is C(left_count, left_count - right_count_r)
                # for each of the chosen number of elements < m before p[i], we can choose the positions of these elements from the number of elements < m before p[i] in i - 1 ways
                # the number of ways to choose the positions of the number of elements < m before p[i] from the number of elements < m before p[i] is (i - 1)^{left_count - right_count_r}
                count += nCr(left_count, left_count - right_count_r) * (i - 1) ** (left_count - right_count_r)
            # if there exists at least one element == m before p[i]
            if mid_count > 0:
                # we need to find the number of elements == m before p[i]
                # for each number of elements == m before p[i] from 1 to mid_count, we can choose the positions of these elements from the number of elements == m before p[i] in i - 1 ways
                # the number of ways to choose the positions of the number of elements == m before p[i] from the number of elements == m before p[i] is (i - 1)^{mid_count}
                count += sum(nCr(mid_count, i) * (i - 1) ** i for i in range(1, mid_count + 1))
        # update the number of elements < m in p[:i], the number of elements == m in p[:i], the number of elements > m in p[:i]
        if p[i] < m:
            left_count -= 1
        elif p[i] > m:
            right_count -= 1
        else:
            mid_count -= 1
        # update the number of elements < m in p[i:], the number of elements == m in p[i:], the number of elements > m in p[i:]
        if p[i] < m:
            right_count_r -= 1
        elif p[i] > m:
            left_count_r -= 1
        else:
            mid_count_r -= 1
    return count

def nCr(n, r):
    """
    return nCr
    """
    f = math.factorial
    return f(n) // f(r) // f(n - r)

# read the input
n, m = map(int, input().split())
p = list(map(int, input().split()))

# solve the problem
res = solve(n, m, p)

# print the result
print(res)
