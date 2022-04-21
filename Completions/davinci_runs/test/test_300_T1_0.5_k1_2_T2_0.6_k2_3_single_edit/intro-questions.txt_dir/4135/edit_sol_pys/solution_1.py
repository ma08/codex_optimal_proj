

n = int(input())
t = input()

# reverse the string
t = t[::-1] # works for both python2 and python3

for i in reversed(range(1, n + 1)):
    if n % i == 0:
        # reverse the substring
        t = t[:i][::-1] + t[i:]

print(t) # works for both python2 and python3
