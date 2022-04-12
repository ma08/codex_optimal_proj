

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


def split_array(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = split_array(left)
    right = split_array(right)

    inc, dec = [], []

    while left and right:
        if left[-1] < right[-1]:
            inc.append(left.pop())
        else:
            dec.append(right.pop())

    inc.extend(left)
    dec.extend(right)

    return inc, dec


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    merge_sort(arr)
    inc, dec = split_array(arr)

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
