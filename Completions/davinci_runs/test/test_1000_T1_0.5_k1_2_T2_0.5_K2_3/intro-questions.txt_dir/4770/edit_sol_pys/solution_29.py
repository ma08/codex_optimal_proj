

#The following is the solution to the problem: http://codeforces.com/problemset/problem/118/A

vowels = ['a', 'o', 'u', 'e', 'i', 'y']

s = input()

s = s.lower()

list = []

for i in range(len(s)):
    if s[i] not in vowels:
        list.append("." + s[i])

print(''.join(list))
