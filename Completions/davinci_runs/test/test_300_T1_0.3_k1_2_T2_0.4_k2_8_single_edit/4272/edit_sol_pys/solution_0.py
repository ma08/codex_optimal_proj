

# ABC081A
# https://atcoder.jp/contests/abs/tasks/abc081_a

N = int(input())
S = input()

count = 0

for i in range(N-2):
    if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
        count += 1


# ABC081B
# https://atcoder.jp/contests/abs/tasks/abc081_b

N = int(input())
A = list(map(int, input().split()))

count = 0

while all(a % 2 == 0 for a in A):
    A = list(map(lambda a: a/2, A))
    count += 1

print(count)
print(count)
