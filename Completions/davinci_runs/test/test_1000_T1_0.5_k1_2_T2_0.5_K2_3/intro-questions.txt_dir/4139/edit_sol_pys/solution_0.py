
n = int(input())

# Count the number of 7, 5, and 3 in the number.
def cnt(num):
    cnt_7 = 0
    cnt_5 = 0
    cnt_3 = 0
    for i in str(num):
        if i == '7':
            cnt_7 += 1
        elif i == '5':
            cnt_5 += 1
        elif i == '3':
            cnt_3 += 1
    return cnt_7, cnt_5, cnt_3

# Check if the number is Shichi-Go-San.
def is_sgs(num):
    cnt_7, cnt_5, cnt_3 = cnt(num)
    if cnt_7 >= 1 and cnt_5 >= 1 and cnt_3 >= 1:
        return True
    else:
        return False

# Count the Shichi-Go-San numbers between 1 and N
cnt_sgs = 0
for i in range(1, n+1):
    if is_sgs(i):
        cnt_sgs += 1
print(cnt_sgs)
