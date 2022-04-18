
def subsequence(string, sub):
    if not sub:  # if sub is empty
        return True
    i = 0 # index of sub
    for c in string:
        if c == sub[i]:
            i += 1
            if i == len(sub): # if i reaches the end of sub
                return True
    return False

def solve(string, sub):
    start = 0 
    end = len(string)
    while start != end:
        mid = (start + end) / 2
        if subsequence(string[:mid], sub): # if sub is a sub sequence of string[:mid]
            end = mid
        else:
            start = mid + 1 # if sub is not a sub sequence of string[:mid]
    return len(string) - end

print solve(raw_input(), raw_input()) # input string and sub
