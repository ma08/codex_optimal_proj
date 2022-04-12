
n = int(input())
t = input()

# reverse the string.
t = t[::-1]  # t[::-1] is the reverse of t

for i in reversed(range(1, n + 1)):
    if n % i == 0:
        # reverse the substring.
        t = t[:i][::-1] + t[i:]  # t[:i] is the first i characters of t

print(t)
