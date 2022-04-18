

def subsequence(string, sub, start):
    if not sub:
        return True
    i = 0
    for c in string[start:]:
        if c == sub[i]:
            i += 1
            if i == len(sub):
                return True
    return False

def solve(string, sub):
    start = 0
    end = len(string)
    while start != end:
        mid = (start + end) / 2
        if subsequence(string, sub, mid):
            end = mid
        else:
            start = mid + 1
    return len(string) - end

print solve(raw_input(), raw_input())
