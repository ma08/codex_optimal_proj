


def main():
    _ = input()
    arr = [int(x) for x in input().split()]

    # max_len = 1
    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)+1):
    #         if j - i <= max_len:
    #             continue
    #         if is_increasing(arr[i:j]):
    #             max_len = j - i

    # print(max_len)

    max_len = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            max_len += 1
        else:
            if i + 1 < len(arr):
                if arr[i] > arr[i + 1]:
                    max_len += 1

    print(max_len)


def is_increasing(arr):
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            return False
    return True


if __name__ == "__main__":
    main()