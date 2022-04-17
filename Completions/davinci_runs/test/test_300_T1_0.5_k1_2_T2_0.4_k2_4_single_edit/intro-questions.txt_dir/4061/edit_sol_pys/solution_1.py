

def subsequence(string, sub):
    if sub == "":
        return True
    for i in range(len(string)):
        if string[i] == sub[0]:
            for j in range(len(sub)):
                if string[i + j] != sub[j]:
                    break
                if j == len(sub) - 1:
                    return True
    return False

def solve(string, sub):
    start, end = 0, len(string)
    while start != end:
        mid = (start + end) // 2
        if subsequence(string[:mid], sub):
            end = mid
        else:
            start = mid + 1
    return len(string) - end

print(solve(input(), input()))
