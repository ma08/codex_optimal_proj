# https://atcoder.jp/contests/abc167/tasks/abc167_a

S = input()

S = list(S)
S.sort()

# print(S)

for i in range(len(S) - 1):
    if ord(S[i]) + 1 < ord(S[i + 1]):
        print(chr(ord(S[i]) + 1))
        break
    elif i == len(S) - 2:
        print(chr(ord(S[i + 1]) + 1))
