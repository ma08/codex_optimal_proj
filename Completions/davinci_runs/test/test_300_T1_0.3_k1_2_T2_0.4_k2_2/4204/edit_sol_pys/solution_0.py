# n = int(input())
# s = input()
# k = int(input())
#
# def next_day(s):
#     next_s = ""
#     for c in s:
#         next_s += c * int(c)
#     return next_s
#
# for i in range(15):
#     s = next_day(s)
#
# print(s[k-1])
#

s = input()
k = int(input())

def next_day(s, k):
    if len(s) == 1:
        return s
    else:
        next_s = ""
        for c in s:
            next_s += c * int(c)
        return next_day(next_s, k)

print(next_day(s, k)[k-1])
