

def subsequence(string, sub):
    if not sub:  # if sub is empty
        return True
    i = 0
    for c in string:  # iterate through string
        if c == sub[i]:
            i += 1  # increment i
            if i == len(sub):
                return True
    return False

def solve(string, sub):
    start = 0  # start of interval
    end = len(string)  # end of interval
    while start != end:  # while start does not equal end
        mid = (start + end) / 2
        if subsequence(string[:mid], sub):  # if subsequence is true
            end = mid
        else:
            start = mid + 1
    return len(string) - end  # return length of string - end

print(solve(raw_input(), raw_input()))
