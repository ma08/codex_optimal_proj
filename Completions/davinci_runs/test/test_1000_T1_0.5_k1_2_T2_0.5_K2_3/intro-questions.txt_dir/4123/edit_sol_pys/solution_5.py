

def solve(s):
    max_count = 0
    max_mer = ""
    for i in range(len(s) - 1):
        mer = s[i:i+2]
        count = s.count(mer)
        if count > max_count:
            max_count = count
            max_mer = mer
    return max_mer

print(solve(s))
