#!/bin/python3

n = int(input())
s = input()

#s = '120110'
#n = len(s)

a = [0,0,0]
for i in range(n):
    a[int(s[i])] += 1

#print(a)

if a[1] == a[2]:
    print(s)
else:
    k = a[1] - a[2] #calculate the difference between 1 and 2
    if k < 0: #if the difference is negative then make it positive
        k = -k 
    r = k // 3 #calculate the number of times 3 can be divided in the difference
    if k % 3 != 0: #if the difference is not divisible by 3 then add 1 to the number of times 3 can be divided in the difference
        r += 1
    #print(r) 
    a[1] -= r #decrease 1 by the number of times 3 can be divided in the difference
    a[2] += r #increase 2 by the number of times 3 can be divided in the difference
    #print(a)
    ans = ''
    for i in range(n): #loop through the length of the string
        if a[0] > 0: #if there are 0's in the array then add 0 to the answer
            ans += '0' 
            a[0] -= 1 #decrease 0 by 1
        elif a[1] > 0: #if there are 1's in the array then add 1 to the answer
            ans += '1' 
            a[1] -= 1 #decrease 1 by 1
        elif a[2] > 0: #if there are 2's in the array then add 2 to the answer
            ans += '2' 
            a[2] -= 1 #decrease 2 by 1
    print(ans)
