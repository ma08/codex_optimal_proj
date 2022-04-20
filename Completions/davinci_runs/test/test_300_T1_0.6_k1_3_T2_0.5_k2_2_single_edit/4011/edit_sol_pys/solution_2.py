
def get_max_number(n, a, f, i):
    # get the max number
    max_num = 0
    for j in range(n):
        max_num = max_num * 10 + f[int(a[j]) - 1]
        if j == i:
            max_num = max_num * 10 + f[int(a[j + 1]) - 1]
            j += 1
    return max_num

def get_max_num_after_operation(n, a, f, i):
    max_num = get_max_number(n, a, f, i)
    for j in range(n):
        if j == i:
            continue
        for k in range(j + 1, n):
            # replace a[j] to a[k]
            a[j], a[k] = a[k], a[j]
            temp_num = get_max_number(n, a, f, j)
            max_num = max(temp_num, max_num)
            # roll back
            a[j], a[k] = a[k], a[j]
    return max_num

if __name__ == '__main__':
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    max_num = get_max_number(n, a, f, -1)
    for i in range(n):
        temp_num = get_max_num_after_operation(n, a, f, i)
        max_num = max(temp_num, max_num)
    print(max_num)
