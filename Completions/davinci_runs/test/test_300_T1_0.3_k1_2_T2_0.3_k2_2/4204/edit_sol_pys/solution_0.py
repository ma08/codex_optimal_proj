

def next_day(s):
    next_s = ""
    for c in s:
        next_s += c * int(c)
    return next_s

def main():
    s = input()
    k = int(input())

print(s[k-1])
