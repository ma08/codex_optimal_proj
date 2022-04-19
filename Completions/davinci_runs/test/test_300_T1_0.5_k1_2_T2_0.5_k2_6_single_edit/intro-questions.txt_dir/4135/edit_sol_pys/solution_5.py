n = int(input())
t = input()

# reverse the string
t = t[::-1]
# reverse the substring

for i in reversed(range(1, n + 1)):
    if n % i == 0:
        t = t[:i][::-1] + t[i:]

print(t)
