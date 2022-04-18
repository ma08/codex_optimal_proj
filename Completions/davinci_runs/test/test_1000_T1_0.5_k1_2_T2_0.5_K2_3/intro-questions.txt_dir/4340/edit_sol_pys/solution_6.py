
def adjacent_replacements_algorithm(a):
    n = len(a)
    b = []
    for i in range(n):
        if a[i] % 2 == 0:
            b.append(a[i] - 1)
        else:
            b.append(a[i])
    return b


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]
    print(*adjacent_replacements_algorithm(a))
