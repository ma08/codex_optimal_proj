

def subsequence(s, t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        i += 1
    return j == len(t)

def solve(s, t):
    if subsequence(s, t):
        return 0
    s = s[::-1]
    t = t[::-1]
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        i += 1
    return len(s) - i

if __name__ == '__main__':
    s = input()
    t = input()
    print(solve(s, t))