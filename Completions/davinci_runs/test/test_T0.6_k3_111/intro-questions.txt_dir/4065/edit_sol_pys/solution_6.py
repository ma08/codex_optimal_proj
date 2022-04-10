
def check_contest(num, prev_diff, max_diff, count):
    if num == 1:
        return count
    elif num == 2:
        return count + 1
    elif num == 3:
        return count + 2
    else:
        if max_diff > 2 * prev_diff:
            return check_contest(num - 1, prev_diff, max_diff, count)
        else:
            return check_contest(num - 1, max_diff, max_diff, count + 1)

num_probs = int(input())
difficulties = [int(x) for x in input().split()]
max_diff = difficulties[-1]
print(check_contest(num_probs, 0, max_diff, 0))
