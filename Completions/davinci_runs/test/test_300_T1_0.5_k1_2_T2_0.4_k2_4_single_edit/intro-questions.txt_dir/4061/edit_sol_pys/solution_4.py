

def subsequence(string, sub):
    if not sub: # if sub is empty
        return True
    i = 0
    for c in string: # iterate through string
        if c == sub[i]:
            i += 1 # if the character matches, move to the next character
            if i == len(sub):
                return True # if all characters match, return true
    return False

def solve(string, sub):
    start = 0 # start of the string
    end = len(string) # end of the string
    while start != end:
        mid = (start + end) / 2 # mid point of the string
        if subsequence(string[:mid], sub): # if the sub is in the first half
            end = mid
        else:
            start = mid + 1 # if the sub is in the second half
    return len(string) - end # return the length of the string minus the end

print solve(raw_input(), raw_input())
