

def subsequence(string, subs):
    if not subs:
        return True
    i = 0
    for c in string:
        if c == subs[i]:
            i += 1
            if i == len(subs):
                return True
    return False

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

print(solve(raw_input(), raw_input()))
