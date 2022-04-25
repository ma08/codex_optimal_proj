

def subsequence(string, subseq):
    if not subseq:
        return True
    i = 0
    for c in string:
        if c == subseq[i]:
            i += 1
            if i == len(subseq):
                return True
    return False

def solve(string, subseq):
    start = 0
    end = len(string)
    while start != end:
        mid = (start + end) / 2
        if subsequence(string[:mid], subseq):
            end = mid
        else:
            start = mid + 1
    return len(string) - end

print(solve(input(), input()))
