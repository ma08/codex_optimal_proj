
def get_max_number(n, a, f):
    # get the max number
    max_num = 0
    for i in range(n):
        max_num = max_num * 10 + f[int(a[i]) - 1]
    return max_num

def get_max_num_after_operation(n, a, f):
    max_num = get_max_number(n, a, f)
    for i in range(n):
        for j in range(i + 1, n):
            # replace a[i] to a[j]
            a[i], a[j] = a[j], a[i]
            temp_num = get_max_number(n, a, f)
            max_num = max(temp_num, max_num)
            # roll back
            a[i], a[j] = a[j], a[i]
    return max_num

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    f = list(map(int, input().split()))
    print(get_max_num_after_operation(n, a, f))
