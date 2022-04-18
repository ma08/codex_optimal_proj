

def simplicity(s):
    return len(set(s)) - 1

def min_erase(S):
    min_erase = len(S)
    for i in range(len(S)):
        S_ = S[:i] + S[i+1:]
        min_erase = min(min_erase, len(S) - simplicity(S_))
    return min_erase + 1

print(min_erase(input()))
