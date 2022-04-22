

n = int(input())
s = input()

def solve(n, s):
    max_count = 0
    max_gram = ""
    for i in range(n - 1):
        gram = s[i:i + 2]
        count = s.count(gram)
        if count > max_count:
            max_count = count
            max_gram = gram
    return max_gram

print(solve(s))
