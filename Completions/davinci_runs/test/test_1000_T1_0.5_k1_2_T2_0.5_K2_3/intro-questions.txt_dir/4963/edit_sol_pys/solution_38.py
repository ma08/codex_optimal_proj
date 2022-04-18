def remove_duplicates(arr):
    if not arr:
        return 0

    write_index = 1
    for i in range(1, len(arr)):
        if arr[write_index - 1] != arr[i]:
            arr[write_index] = arr[i]
            write_index += 1

    return write_index


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()
