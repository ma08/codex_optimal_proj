

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def split_arr(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = split_arr(left)
    right = split_arr(right)

    inc_arr = []
    dec_arr = []

    while left and right:
        if left[-1] < right[-1]:
            inc_arr.append(left.pop())
        else:
            dec_arr.append(right.pop())

    inc_arr.extend(left)
    dec_arr.extend(right)

    return inc_arr, dec_arr


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    merge_sort(arr)
    inc, dec = split_arr(arr)

    if len(inc) + len(dec) != n:
        print('NO')
    else:
        print('YES')
        print(len(inc))
        print(*inc)
        print(len(dec))
        print(*dec)


if __name__ == '__main__':
    main()
