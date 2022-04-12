
# check if palindrome, if not, find the minimum number of operations to make it palindrome
s = input().strip()

if s == s[::-1]:
    print(0)
    exit()

# if s[i] != s[-1 - i], then s[i] != s[-1 - i] and s[i + 1] != s[-1 - i - 1]
# so we can delete either s[i] or s[-1 - i]
print(1)
