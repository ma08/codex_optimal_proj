
n = int(input())

# Count the number of 7, 5, 3 in the number
def count(number):
    cnt_7 = number.count('7')
    cnt_5 = number.count('5')
    cnt_3 = number.count('3')
    return cnt_7, cnt_5, cnt_3

# Check if the number is Shichi-Go-San
def is_sgs(num):
    cnt_7, cnt_5, cnt_3 = cnt(num)
    if cnt_7 >= 1 and cnt_5 >= 1 and cnt_3 >= 1:
        return True
    else:
        return False

# Count the Shichi-Go-San between 1 and N
cnt_sgs = 0
for i in range(1, n+1):
    if is_sgs(i):
        cnt_sgs += 1
print(cnt_sgs)
