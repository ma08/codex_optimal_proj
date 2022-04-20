
n = int(input())
t = input()

# reverse the string
t = t[::-1]

for i in range(n, 0, -1):
    if n % i == 0:
        # reverse the substring
        t = t[:i][::-1] + t[i:]

print(t)
