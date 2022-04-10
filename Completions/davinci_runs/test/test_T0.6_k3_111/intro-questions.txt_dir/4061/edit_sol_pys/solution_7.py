
def subseq(s, t):
    i = 0
    for c in s:
        if i < len(t) and c == t[i]:
            i += 1

    return i == len(t)
    # s = input()
    # t = input()

def main():
    s = input()
    t = "abc"
    i = 0
    j = 0
    best = 0
    while True:
        while j < len(s) and subseq(s[i:j + 1], t):
            best = max(best, j - i + 1)
            j += 1
        if j >= len(s):
            break
        i += 1
        j = max(j, i)
    print(len(s) - best)


if __name__ == '__main__':
    main()
