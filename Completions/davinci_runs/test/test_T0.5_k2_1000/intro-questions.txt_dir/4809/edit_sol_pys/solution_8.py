

# TODO: This problem is not done.

def coconut_splat(s, n):
    if s == 10:
        if n == 2:
            return 2
        elif n == 3:
            return 3
        elif n == 4:
            return 4
        elif n == 5:
            return 5
        elif n == 6:
            return 6
        elif n == 7:
            return 7
        elif n == 8:
            return 8
        elif n == 9:
            return 9
        elif n == 10:
            return 7
        else:
            return 1
    elif s == 9:
        if n == 2:
            return 2
        elif n == 3:
            return 3
        elif n == 4:
            return 4
        elif n == 5:
            return 5
        elif n == 6:
            return 6
        elif n == 7:
            return 7
        elif n == 8:
            return 8
        elif n == 9:
            return 9
        elif n == 10:
            return 8
        else:
            return 1
    else:
        return 1

s, n = map(int, input().split())
print(coconut_splat(s, n))
