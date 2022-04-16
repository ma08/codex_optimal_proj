

# def play_coconut_splat(s, n):
#     if s % 2 == 0:
#         return (s // 2) % n + 1
#     else:
#         return s // 2 % n + 1

# print(play_coconut_splat(int(input()), int(input())))


def find_max_sum(a, n):
    if n == 1:
        return a[0]
    if n == 2:
        return max(a[0], a[1])
    return max(find_max_sum(a, n-1), find_max_sum(a, n-2) + a[n-1])


# Driver program to test above function
a = [5, 5, 10, 100, 10, 5]
print(find_max_sum(a, len(a)))
