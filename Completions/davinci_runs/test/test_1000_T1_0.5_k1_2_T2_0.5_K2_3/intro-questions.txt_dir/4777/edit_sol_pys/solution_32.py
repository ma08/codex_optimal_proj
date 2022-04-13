
def max_sequence(n):
    max_sum = 0
    for i in range(len(n) + 1):
        for j in range(i, len(n) + 1):
            this_sum = 0
            for k in range(i, j + 1):
                this_sum += n[k]
            if this_sum > max_sum:
                max_sum = this_sum
    return max_sum


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4, 5, 6, 7]))
