
n = int(input())  # input the number
t = input()
s = [""] * n  # initialize the list

# reverse the string
t = t[::-1]

for i in reversed(range(1, n + 1)):
    if n % i == 0:
        # reverse the substring
        t = t[:i][::-1] + t[i:]

print(t)
