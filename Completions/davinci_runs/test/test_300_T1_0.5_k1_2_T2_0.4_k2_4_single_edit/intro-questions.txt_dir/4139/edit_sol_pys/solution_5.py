

n = int(input())

# Count the number of 7, 5 and 3 in the number
def cnt(num):
    cnt7 = 0
    cnt5 = 0
    cnt3 = 0
    for i in str(num):
        if i == '7':
            cnt7 += 1
        elif i == '5':
            cnt5 += 1
        elif i == '3':
            cnt3 += 1
    return cnt7, cnt5, cnt3

# Check if the number is Shichi-Go-San number
def is_sgs(num):
    cnt7, cnt5, cnt3 = cnt(num)
    if cnt7 >= 1 and cnt5 >= 1 and cnt3 >= 1:
        return True
    else:
        return False

# Count the Shichi-Go-San numbers between 1 and N
cntsgs = 0
for i in range(1, n+1):
    if is_sgs(i):
        cntsgs += 1
print(cntsgs)
