
def get_max_number(n, a, f, flag):
    # get the max number
    max_num = 0
    for i in range(n):
        if flag[i]:
            max_num = max_num * 10 + f[int(a[i]) - 1]
        else:
            max_num = max_num * 10 + a[i]
    return max_num

def get_max_num_after_operation(n, a, f):
    flag = [True] * n
    max_num = get_max_number(n, a, f, flag)
    for i in range(n):
        for j in range(i + 1, n):
            # replace a[i] to a[j]
            a[i], a[j] = a[j], a[i]
            flag[i], flag[j] = False, False
            temp_num = get_max_number(n, a, f, flag)
            max_num = max(temp_num, max_num)
            # roll back
            a[i], a[j] = a[j], a[i]
            flag[i], flag[j] = True, True
    return max_num

if __name__ == '__main__':
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    print(get_max_num_after_operation(n, a, f))
