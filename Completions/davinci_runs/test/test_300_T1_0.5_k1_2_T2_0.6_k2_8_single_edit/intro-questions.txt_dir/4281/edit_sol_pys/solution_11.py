
# questions:
# 1) what is the max length of the sequence?
# 2) can there be duplicates?
# 3) can the sequence be empty?


def get_count(x):
    min_cnt = 0
    max_cnt = 0

    # min
    curr = x[0]
    min_cnt = 1
    for i in range(1, len(x)):
        if x[i] != curr:
            curr = x[i]
            min_cnt += 1

    # max
    curr = x[0]
    max_cnt = 1
    for i in range(1, len(x)):
        if x[i] != curr:
            curr = x[i]
            max_cnt += 1
        elif x[i] == curr and i == len(x)-1:
            max_cnt += 1

    return (min_cnt, max_cnt)



n = int(input())
x = str(input())

min_cnt, max_cnt = get_count(x)

print(min_cnt, max_cnt)
