# https://codeforces.com/problemset/problem/1159/A

N = int(input())

count = 0
for i in range(N):
    word = input()
    word = word.lower()
    if "pink" in word or "rose" in word:
        count += 1

if count > 0:
    print(count)
else:
    print("I must watch Star Wars with my daughter")
