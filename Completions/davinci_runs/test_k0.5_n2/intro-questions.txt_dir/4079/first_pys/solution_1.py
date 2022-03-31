

# SOLUTION

n = int(input())
for _ in range(n):
    s = input()
    if len(s) != len(set(s)):
        print("No")
    else:
        a = ord(s[0])
        for i in s[1:]:
            a += 1
            if i != chr(a):
                print("No")
                break
        else:
            print("Yes")