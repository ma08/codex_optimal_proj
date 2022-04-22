

def subsequence(string, sub):
    if not sub:
        return True
    for i in range(len(string)):
        if string[i] == sub[0]:
            if sub == string[i:i+len(sub)]:
                return i
    return False

def solve(string, sub):
    return subsequence(string, sub)

print solve(raw_input(), raw_input())
