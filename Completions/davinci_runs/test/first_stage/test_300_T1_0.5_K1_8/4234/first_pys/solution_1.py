

n = int(input())
s = input()

# If the string is already good, print 0 and the string
if n % 2 == 0 and len(set(s[::2])) == len(set(s[1::2])):
    print(0)
    print(s)

# Otherwise, find the index of the first repeated letter
else:
    if n % 2 == 0:
        i = 0
        while i < n:
            if s[i] == s[i+1]:
                break
            i += 2
        print(i+1)
        print(s[:i] + s[i+2:])

    else:
        i = 1
        while i < n:
            if s[i] == s[i+1]:
                break
            i += 2
        print(i+1)
        print(s[:i] + s[i+2:])