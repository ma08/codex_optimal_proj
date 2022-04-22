# print all permutations of string

def permutation(s):
    if len(s) == 1:
        return s
    else:
        perm = []
        for i in range(len(s)):
            for j in permutation(s[:i] + s[i+1:]):
                perm.append(s[i] + j)
        return perm

s = input()

for i in permutation(s):
    print(i)
