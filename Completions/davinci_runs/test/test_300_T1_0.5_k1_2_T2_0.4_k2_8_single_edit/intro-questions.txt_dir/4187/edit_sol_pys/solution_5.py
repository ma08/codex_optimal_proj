


def get_max_rest(a):
    max_rest = 0
    rest = 0

    for i in a:
        if i == 0:
            max_rest = max(max_rest, rest)
            rest = 0
        else:
            rest += 1

    max_rest = max(max_rest, rest)
    return max_rest


n = int(input())
a = list(map(int, input().split()))

max_rest = get_max_rest(a)
print(max_rest)
