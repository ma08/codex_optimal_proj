

#-----Solution-----

n, x, y = [int(i) for i in input().split()]
num = input()

#calculate the remainder of the input number
rem = 0
for i in range(n-1, n-x-1, -1):
    rem = rem*2 + int(num[i])

#calculate the remainder of the desired number
rem_des = 0
for i in range(n-1, n-x-1, -1):
    if i >= n-y:
        rem_des = rem_des*2 + 1
    else:
        rem_des = rem_des*2

print(min(rem, rem_des - rem))