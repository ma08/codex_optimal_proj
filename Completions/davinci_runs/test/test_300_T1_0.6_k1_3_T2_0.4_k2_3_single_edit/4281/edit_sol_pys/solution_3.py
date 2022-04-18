

def get_answer(x):
    x.sort()
    if len(x) == 1:
        return 1, 1

    min_count, max_count = 1, 1

    i = 1
    while i < len(x):
        if x[i] - x[i-1] == 1:
            min_count += 1
            i += 1
        else:
            i += 1

    i = 1
    while i < len(x):
        if x[i] - x[i-1] == 1:
            max_count += 1
            i += 1
        else:
            max_count += 1
            i += 1

    return min_count, max_count


if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().split()))
    answer = get_answer(x)
    print("{} {}".format(answer[0], answer[1]))
