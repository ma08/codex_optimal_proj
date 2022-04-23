

def subsequence(string, sub_seq):
    if not sub_seq:
        return True
    i = 0
    for c in string:
        if c == sub_seq[i]:
            i += 1
            if i == len(sub_seq):
                return True
    return False

def solve(string, sub_seq):
    start = 0
    end = len(string)
    while start != end:
        mid = (start + end) / 2
        if subsequence(string[:mid], sub_seq):
            end = mid
        else:
            start = mid + 1
    return len(string) - end

print solve(raw_input(), raw_input())
