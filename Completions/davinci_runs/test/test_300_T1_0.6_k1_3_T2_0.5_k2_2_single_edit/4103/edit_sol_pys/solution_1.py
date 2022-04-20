

n, b, a = map(int, input().split())  # читаем входные данные
s = list(map(int, input().split()))


def solve_problem(n, b, a, s):
    max_segments = 0
    cur_a = a
    cur_b = b
    for i in range(n):
        if s[i] == 1:
            if cur_b > 0:
                cur_b -= 1
                cur_a += 1
                if cur_a > a:
                    cur_a = a
            else:
                cur_a -= 1
        else:
            if cur_a > 0:
                cur_a -= 1
            else:
                cur_b -= 1
        if cur_a == 0 and cur_b == 0:
            break
        max_segments += 1
    return max_segments


print(solve_problem(n, b, a, s))
