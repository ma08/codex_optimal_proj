

def hamming_distance(s, t):
    return sum(c1 != c2 for c1, c2 in zip(s, t))

def swap_letters(s, t):
    if hamming_distance(s, t) == 0:
        return 0, -1, -1
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            s_new = s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]
            if hamming_distance(s_new, t) == 1:
                return 1, i + 1, j + 1
    return 2, -1, -1

def main():
    n = int(input())
    s = input()
    t = input()
    x, i, j = swap_letters(s, t)
    print(x)
    print(i, j)

if __name__ == "__main__":
    main()