

def check_contest(num, prev_diff, max_diff):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 3
    else:
        if max_diff > 2 * prev_diff:
            return check_contest(num - 1, prev_diff, max_diff)
        else:
            return check_contest(num - 1, max_diff, max_diff)

num_probs = int(input())
difficulties = [int(x) for x in input().split()]
max_diff = difficulties[-1]
print(check_contest(num_probs, 0, max_diff))