

def subsequence(string, sub):
    if not sub:
        return True
    i = 0
    for c in string:
        if c == sub[i]:
            i += 1
            if i == len(sub):
                return True
    return False

def solve(string, sub, start = 0):
    start = 0
    end = len(string)
    while end - start > 1:
        mid = (start + end) / 2
        if subsequence(string[:mid], sub):
            end = mid
        else:
            start = mid + 1
    return len(string) - end + start

def main():
    string = raw_input()
    sub = raw_input()
    print solve(string, sub)

if __name__ == "__main__":
    main()
