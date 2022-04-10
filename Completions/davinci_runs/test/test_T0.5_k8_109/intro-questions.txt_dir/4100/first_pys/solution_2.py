

n, k, q = map(int, input().split())
a_list = [int(input()) for i in range(q)]

score_list = [k - q] * n
for a in a_list:
    score_list[a - 1] += 1

for score in score_list:
    if score > 0:
        print("Yes")
    else:
        print("No")