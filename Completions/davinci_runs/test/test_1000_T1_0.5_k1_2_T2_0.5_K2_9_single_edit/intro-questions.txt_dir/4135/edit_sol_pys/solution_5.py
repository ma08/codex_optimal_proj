

n = int(input())  # number of characters
t = input()  # string

s = [""] * n  # list of characters

# reverse the string
t = t[::-1]  # t[start:end:step]

for i in reversed(range(1, n + 1)):
    if n % i == 0:
        # reverse the substring
        t = t[:i][::-1] + t[i:]

print(t)
