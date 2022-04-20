

s = input()
k = int(input())

# k = 1
# for i in range(1, 16):
#     k *= 10

# print(s)
# print(k)

def rec(s, k):
    # print(s)
    # print(k)
    if k == 1:
        return s[0]
    if k <= len(s):
        return s[k-1]
    else:
        new = ""
        for i in s:
            new += int(i) * str(i)
        return rec(new, k)

print(rec(s, k))