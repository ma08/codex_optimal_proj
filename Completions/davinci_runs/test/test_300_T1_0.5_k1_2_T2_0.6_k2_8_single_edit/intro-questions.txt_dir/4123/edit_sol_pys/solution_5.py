
n = int(input())
s = input()

def solve(s):
    max_count = 0
    max_gram = ""
    for i in range(len(s) - 1):  # for each gram
        gram = s[i:i + 2]
        count = s.count(gram)
        if count > max_count:  # new max
            max_count = count
            max_gram = gram
    return max_gram

print(solve(s))
