

def solution():
    # Solution here
    n = int(input())
    s = input()
    # print(n, s)

    # count the number of question marks
    k = 0
    for i in range(n):
        if s[i] == '?':
            k += 1
    # print(k)

    # count the number of subsequences "abc" in the original string
    cnt = 0
    for i in range(n - 2):
        if s[i] == 'a' and s[i + 1] == 'b' and s[i + 2] == 'c':
            cnt += 1
    # print(cnt)

    # count the number of subsequences "abc" in all strings we can obtain if we replace
    # all question marks with letters "a", "b" and "c"
    res = 3 ** k * cnt

    # print the result modulo $10^{9} + 7$
    print(res % (10 ** 9 + 7))


solution()