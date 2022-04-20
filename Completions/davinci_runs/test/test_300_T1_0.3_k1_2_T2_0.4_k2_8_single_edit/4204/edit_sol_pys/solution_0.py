
def next_day(s):
    next_s = ""
    for c in s:
        next_s += c * int(c)
    return next_s

if __name__ == "__main__":
    s = input()
    k = int(input())

print(s[k-1])
