

def subsequence(string, sub):
    for c in sub:
        if c not in string:
            return False
    return True

def solve(string, sub):
    start = 0
    end = len(string)
    while start != end:
        mid = (start + end) / 2
        if subsequence(string[:mid], sub):
            end = mid
        else:
            start = mid + 1
    return len(string) - end

print solve(raw_input(), raw_input())
