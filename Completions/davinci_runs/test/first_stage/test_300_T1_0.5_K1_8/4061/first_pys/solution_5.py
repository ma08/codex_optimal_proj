

def subsequence(s1, s2):
    if len(s2) == 0:
        return True
    if len(s1) == 0:
        return False

    if s1[0] == s2[0]:
        return subsequence(s1[1:], s2[1:])
    else:
        return subsequence(s1[1:], s2)

def max_removal(s, t):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if subsequence(s[:i] + s[j:], t):
                return len(s) - len(t)
    return 0

def main():
    s = input()
    t = input()
    print(max_removal(s, t))

if __name__ == '__main__':
    main()