#https://atcoder.jp/contests/abc076/tasks/abc076_a

#-----main-----

#input
S = input()
T = input()

#initialize
count = 0

#count the number of differences
for i in range(len(S)):
    if S[i] != T[i]:
        count += 1

#output
print(count)
