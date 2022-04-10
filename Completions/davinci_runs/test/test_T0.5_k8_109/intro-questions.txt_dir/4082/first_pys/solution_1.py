

# n = int(input())
# a = list(map(int, input().split()))

def max_increasing_subarray(a):
    if len(a) == 1:
        return 1
    if len(a) == 2:
        return 2
    max_len = 0
    for i in range(len(a)):
        if i == 0:
            tmp = [a[i], a[i+1]]
        elif i == len(a) - 1:
            tmp = [a[i-1], a[i]]
        else:
            tmp = [a[i-1], a[i], a[i+1]]
        tmp.sort()
        if tmp[1] == a[i]:
            cur_len = 0
            for j in range(len(a)):
                if a[j] < a[i]:
                    continue
                cur_len += 1
                if j == len(a) - 1 or a[j+1] <= a[i]:
                    break
            max_len = max(max_len, cur_len)
    return max_len

assert(max_increasing_subarray([1,2,5,3,4]) == 4)
assert(max_increasing_subarray([1,2]) == 2)
assert(max_increasing_subarray([6,5,4,3,2,4,3]) == 2)