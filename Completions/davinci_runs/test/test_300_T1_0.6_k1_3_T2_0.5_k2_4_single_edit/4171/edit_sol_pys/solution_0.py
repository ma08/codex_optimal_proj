
def run(arr, k):
    count = 0
    while len(set(arr)) > 1:
        count += 1
        if min(arr) == 0:
            arr.remove(0)
        arr = list(map(lambda x: x // 2, arr))
        if min(arr) == 0:
            arr.remove(0)
    if len(set(arr)) == 1 and arr.count(arr[0]) >= k:
        return count
    else:
        return -1


print(run(arr, k))
