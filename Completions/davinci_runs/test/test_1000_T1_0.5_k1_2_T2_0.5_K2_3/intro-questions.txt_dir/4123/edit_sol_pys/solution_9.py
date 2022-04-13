

n = int(input())
s = input()

def solve(s):
    max_count = 1
    max_pair = s[0:2]
    for i in range(len(s) - 1):
        pair = s[i:i+2]
        count = s.count(pair)
        if count > max_count:
            max_count = count
            max_pair = pair
    return max_pair

print(solve(s))
