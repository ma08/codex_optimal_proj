

def get_answer(n, x):
    if n == 1:
        return 1

    min_count = 1
    max_count = 1

    i = 1
    while i < n:
        if x[i] - x[i-1] == 1:
            min_count += 1
            i += 2
        else:
            i += 1

    i = 1
    while i < n:
        if x[i] - x[i-1] == 1:
            max_count += 1
            i += 2
        else:
            max_count += 1
            i += 1

    return max_count - min_count


if __name__ == "__main__":
    n = int(input())
    x = sorted(list(map(int, input().split())))
    answer = get_answer(n, x)
    print(answer)
