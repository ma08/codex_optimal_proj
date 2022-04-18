# https://atcoder.jp/contests/abc136/tasks/abc136_b
# https://atcoder.jp/contests/abc136/submissions/13180851


n = input()

n = int(n)
count = 0
for i in range(1, n + 1):
    if len(str(i)) % 2 == 1:
        count += 1

print(count)
