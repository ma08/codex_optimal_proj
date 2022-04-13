

def max_sequence(n):
    max_sum = n[0]
    for i in range(len(n)):
        for j in range(i, len(n)):
            this_sum = 0
            for k in range(i, j):
                this_sum += n[k]
            if this_sum > max_sum:
                max_sum = this_sum
    return max_sum


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4, 6]))
