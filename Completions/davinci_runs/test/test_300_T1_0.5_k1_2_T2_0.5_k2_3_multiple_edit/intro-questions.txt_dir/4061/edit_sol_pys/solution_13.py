

def subsequence(string, sub_string):
    if not sub_string:
        return True
    i = 0
    for c in string:
        if c == sub_string[i]:
            i += 1
            if i == len(sub_string):
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

print solve(raw_input(), raw_input())
