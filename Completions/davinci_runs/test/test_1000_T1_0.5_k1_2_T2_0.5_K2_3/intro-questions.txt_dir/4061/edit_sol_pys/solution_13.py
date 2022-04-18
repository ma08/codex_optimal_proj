

def subsequence(string, subseq, start, end):
    if not subseq:
        return True
    i = 0
    for c in string[start:end]:
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
        if subsequence(string, subseq, start, mid):
            end = mid
        else:
            start = mid + 1
    return len(string) - end

print solve(raw_input(), raw_input())
