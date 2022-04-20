import sys
input = sys.stdin.readline


n = int(input())  # int
s = input()  # str
l = list(map(int, input().split()))  # list of int
s = list(input())  # list of str
d = {}  # dict

# for i in range(n):
#     l.append(int(input()))

count = 0

for i in range(n - 2):
    if s[i] == "A" and s[i + 1] == "B" and s[i + 2] == "C":
        count += 1


# print("{} {}".format(n, s))
print(count)
