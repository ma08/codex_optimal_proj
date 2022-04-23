

# input
a, b, c = map(int, input().split()) # a: 初期値, b: 目標値, c: 回数

# count up (while)
count = 0
while b >= a and count < c:
    b -= a
    count += 1

# output (print)
print(count)
