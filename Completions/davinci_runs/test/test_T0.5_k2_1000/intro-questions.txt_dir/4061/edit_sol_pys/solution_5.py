

def subseq(string, sub):
    if len(sub) == 0:
        return True
    for i in range(len(string)):
        if string[i] == sub[0]:
            if subseq(string[i+1:], sub[1:]):
                return True
    return False

def solve(string, sub):
    start = 0
    end = len(string)
    while start < end:
        mid = (start + end) / 2
        if subseq(string[:mid], sub):
            end = mid
        else:
            start = mid + 1
    return len(string) - end

print solve(raw_input(), raw_input())
