

def substring(string, sub):
    if not sub: 
        return True
    for i in range(len(string)):
        if string[i] == sub[0]:
            j = 0
            while j < len(sub) and string[i + j] == sub[j]:
                j += 1
            if j == len(sub):
                return True 
    return False 

def solve(string, sub):
    start = 0
    end = len(string)
    while start < end:
        mid = (start + end) // 2
        if substring(string[:mid], sub):
            end = mid
        else:
            start = mid + 1
    return len(string) - end

print solve(raw_input(), raw_input())
