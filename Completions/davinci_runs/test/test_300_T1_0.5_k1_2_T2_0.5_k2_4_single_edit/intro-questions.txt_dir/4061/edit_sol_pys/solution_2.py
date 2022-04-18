

def subsequence(string, sub, i=0):
    if not sub or i >= len(string):
        return True
    if string[i] == sub[0]:
        return subsequence(string, sub[1:], i + 1)
    return subsequence(string, sub, i + 1)

def solve(string, sub):
    start = 0
    end = len(string)
    while start != end:
        mid = (start + end) / 2
        if subsequence(string[:mid], sub):
            end = mid
        else:
            start = mid + 1
    return string[:end]
