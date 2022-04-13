def split_array(arr: list) -> int:
    result = 0
    for i in range(len(arr) - 1):
        if sum(arr[:i + 1]) == sum(arr[i + 1:]):
            result = i + 1
    return result
