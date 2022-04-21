# https://atcoder.jp/contests/abc095/tasks/abc095_a

n = int(input())
num = [int(i) for i in input().split()]

for i in num:
    if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:
        print("DENIED")
        exit()

print("APPROVED")
