
def get_max_number(n, a, f, m):
    # get the max number
    max_num = 0
    for i in range(n):
        max_num = max_num * m + f[int(a[i]) - 1]
    return max_num

def get_max_num_after_operation(n, a, f, m):
    max_num = get_max_number(n, a, f, m)
    for i in range(n):
        for j in range(i + 1, n):
            # replace a[i] to a[j]
            a[i], a[j] = a[j], a[i]
            temp_num = get_max_number(n, a, f, m)
            max_num = max(temp_num, max_num)
            # roll back
            a[i], a[j] = a[j], a[i]
    return max_num

if __name__ == '__main__':
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    m = max(f) + 1
    print(get_max_num_after_operation(n, a, f, m))
