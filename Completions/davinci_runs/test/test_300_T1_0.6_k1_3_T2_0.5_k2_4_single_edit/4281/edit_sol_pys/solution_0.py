

def get_answer(n, x):
    if n == 1:
        return 1

    min_count = 1

    i = 1
    while i < len(x):
        if x[i] - x[i-1] <= 2:
            min_count += 1
        else:
            i += 1

    return min_count


if __name__ == "__main__":
    n = int(input())
    x = sorted(list(map(int, input().split())))
    answer = get_answer(n, x)
    print(answer)
