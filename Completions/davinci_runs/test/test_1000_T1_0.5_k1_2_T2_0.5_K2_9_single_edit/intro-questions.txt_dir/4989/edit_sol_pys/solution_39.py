
n = int(input())
pieces = [int(x) for x in input().split()]


def play(n: int, pieces: list) -> tuple:
    if n == 1:
        return pieces[0], 0
    elif n == 2:
        return max(pieces[0], pieces[1]), min(pieces[0], pieces[1])
    else:
        if pieces[0] > pieces[-1]:
            a, b = play(n - 1, pieces[1:])
            return pieces[0] + b, a
        else:
            a, b = play(n - 1, pieces[:-1])
            return a, pieces[-1] + b

a, b = play(n, pieces)
print(a, b)
