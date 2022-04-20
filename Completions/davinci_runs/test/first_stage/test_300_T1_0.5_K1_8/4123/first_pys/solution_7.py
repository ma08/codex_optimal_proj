

def two_gram(n, s):
    max_count = 0
    max_two_gram = ''
    for i in range(n - 1):
        two_gram = s[i:i+2]
        count = s.count(two_gram)
        if count > max_count:
            max_count = count
            max_two_gram = two_gram
    return max_two_gram

n = int(input())
s = input()
print(two_gram(n, s))