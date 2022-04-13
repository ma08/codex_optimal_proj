
s = input()

def solve(s):
    max_count = 1
    max_mer = s[0]
    for i in range(len(s) - 1):
        mer = s[i:i+2]
        count = s.count(mer)
        if count > max_count:
            max_count = count
            max_mer = mer
    return max_mer

print(solve(s))
