

def main():
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    t = input()
    """
    n = 6
    s = "abcdef"
    t = "abdfec"
    #s = "abcd"
    #t = "accd"

    result = swapLexOrder(s, t, n)

    print(result)
    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()

def swapLexOrder(s, t, n):
    if s == t:
        return 0
    if n == 1:
        if s != t:
            return -1
    if n == 2:
        if s[0] != t[0]:
            return -1
        if s[1] == t[1]:
            return 0
        else:
            return 1
    if s[0] != t[0]:
        return -1
    if s[-1] != t[-1]:
        return -1

    ans = 0
    for i in range(1, n-1):
        if s[i] != t[i]:
            ans += 1

    for i in range(1, n-1):
        if s[i] != t[i]:
            if s[i+1] == t[i]:
                s = s[:i] + t[i] + s[i+1:]
                ans -= 1
            elif s[i-1] == t[i]:
                s = s[:i-1] + t[i] + s[i] + s[i-1]
            else:
                return -1

    return ans

if __name__ == '__main__':
    main()
