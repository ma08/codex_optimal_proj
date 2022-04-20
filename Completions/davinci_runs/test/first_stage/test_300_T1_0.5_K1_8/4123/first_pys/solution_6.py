

def two_grams(s):
    s = list(s)
    max_gram = ''
    max_count = 0
    for i in range(1, len(s)):
        gram = s[i-1] + s[i]
        count = s.count(gram)
        if count > max_count:
            max_count = count
            max_gram = gram
    return max_gram

if __name__ == "__main__":
    n = int(input())
    s = str(input())
    print(two_grams(s))