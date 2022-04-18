

def subsequence(string, subsequence):
    if not subsequence:
        return True
    i = 0
    for c in string:
        if c == subsequence[i]:
            i += 1
            if i == len(subsequence):
                return True
    return False

def solve(string, subsequence):
    start = 0
    end = len(string)
    while start != end:
        mid = (start + end) / 2
        if subsequence(string[:mid], subsequence):
            end = mid
        else:
            start = mid + 1
    return len(string) - end

print solve(raw_input(), raw_input())
