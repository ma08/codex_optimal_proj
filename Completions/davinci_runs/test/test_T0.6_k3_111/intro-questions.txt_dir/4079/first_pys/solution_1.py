

n = int(input())

for i in range(n):
    s = input()
    if len(s) == len(set(s)) and ord(min(s)) + len(s) - 1 == ord(max(s)):
        print("Yes")
    else:
        print("No")