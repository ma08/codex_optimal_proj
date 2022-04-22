

n = int(input())
s = input()

def solve(s):
    max_count = 0
    max_gram = ""
    for i in range(len(s) - 1): # s = "abcd" -> i = 0, 1, 2
        gram = s[i:i+2] # gram = "ab", "bc", "cd"
        count = s.count(gram)
        if count > max_count:
            max_count = count
            max_gram = gram
    return max_gram

print(solve(s))
