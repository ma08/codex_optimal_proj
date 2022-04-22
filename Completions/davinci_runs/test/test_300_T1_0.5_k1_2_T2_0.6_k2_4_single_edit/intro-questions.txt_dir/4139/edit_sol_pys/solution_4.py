
n = int(input())


def is_sgs(num, cnt_7, cnt_5, cnt_3):
    if cnt_7 >= 1 and cnt_5 >= 1 and cnt_3 >= 1 and num < 1000:
        return True
    else:
        return False


# Count the Shichi-Go-San numbers between 1 and N
cnt_sgs = 0
for i in range(1, n+1):
    if is_sgs(i):
        cnt_sgs += 1
print(cnt_sgs)
