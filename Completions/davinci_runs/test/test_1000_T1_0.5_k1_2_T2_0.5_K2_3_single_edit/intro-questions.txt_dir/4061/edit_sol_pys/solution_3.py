

def subsequence(string, sub):
    i = 0
    for c in string:
        if c == sub[i]:
            i += 1
            if i == len(sub):
                return True
    return False

def solve(string, sub):
    if not sub:
        return 0
    ans = len(string)
    for i in range(len(string)):
        for j in range(i, len(string)):
            if subsequence(string[i:j+1], sub):
                ans = min(ans, j - i + 1)
    return ans

print solve(raw_input(), raw_input())
