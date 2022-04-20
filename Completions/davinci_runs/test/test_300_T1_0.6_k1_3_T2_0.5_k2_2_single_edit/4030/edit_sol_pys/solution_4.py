
# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
def countingValleys(n, s):
    level = 0
    res = 0
    for i in s:
        if i == 'U':
            level += 1
        else:
            level -= 1
        if level == 0 and i == 'U':
            res += 1
    return res
