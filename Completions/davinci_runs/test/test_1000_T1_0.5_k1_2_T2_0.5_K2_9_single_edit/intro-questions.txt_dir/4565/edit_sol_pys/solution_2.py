

N = int(input())
S = input()

# 左から右に見ていき、人が向きを変える必要がある場合のカウントを行う
count = 0
curr_dir = "E"
for s in S:
    if s == curr_dir:
        count += 1
    curr_dir = s


print(count)
