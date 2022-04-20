


def rotate_string(s):
    return s[-1] + s[:-1]


def is_rotation(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        rotated_s = rotate_string(s)
        if rotated_s == t:
            return True
        s = rotated_s
    return False


def main():
    s = input()
    t = input()
    if is_rotation(s, t):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()