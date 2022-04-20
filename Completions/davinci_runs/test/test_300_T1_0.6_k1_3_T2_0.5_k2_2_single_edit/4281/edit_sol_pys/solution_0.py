

def get_answer(n, x):
    if n == 1:
        return 1

    x.sort(reverse=True)
    max_count = 1

    i = 1
    while i < n:
        if x[i] == x[i-1]:
            max_count += 1
        i += 1

    return max_count


if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().split()))
    answer = get_answer(n, x)
    print("{}".format(answer))
