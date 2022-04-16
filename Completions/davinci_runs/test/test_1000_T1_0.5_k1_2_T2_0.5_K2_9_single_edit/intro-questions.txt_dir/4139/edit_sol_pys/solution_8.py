
n = int(input())
# Count the number of 7, 5, and 3 in the number
def cnt(num):
    cnt_seven = 0
    cnt_five = 0
    cnt_three = 0
    for i in str(num):
        if i == '7':
            cnt_seven += 1
        elif i == '5':
            cnt_five += 1
        elif i == '3':
            cnt_three += 1
    return cnt_seven, cnt_five, cnt_three

# Check if the number is Shichi-Go-San number
def is_sgs(num):
    cnt_seven, cnt_five, cnt_three = cnt(num)
    if cnt_seven >= 1 and cnt_five >= 1 and cnt_three >= 1:
        return True
    else:
        return False

# Count the Shichi-Go-San numbers between 1 and n
cnt_sgs = 0
for i in range(1, n+1):
    if is_sgs(i):
        cnt_sgs += 1
print(cnt_sgs)
