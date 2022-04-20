


def main():
    s = input()
    t = input()
    # print(s, t)
    print(len(s) + len(t) - 2 * common_prefix_length(s, t))


def common_prefix_length(s, t):
    """
    >>> common_prefix_length("test", "west")
    2
    >>> common_prefix_length("codeforces", "yes")
    2
    >>> common_prefix_length("test", "yes")
    0
    >>> common_prefix_length("b", "ab")
    1
    >>> common_prefix_length("codeforces", "codeforces")
    9
    """
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            return i
    return min(len(s), len(t))


if __name__ == "__main__":
    main()