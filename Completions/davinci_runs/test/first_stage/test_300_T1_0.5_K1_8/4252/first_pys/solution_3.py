

def remove_x(n, s):
    for i in range(n-2):
        if s[i:i+3] == "xxx":
            return 1
    return 0

n = int(input())
s = input()

print(remove_x(n, s))