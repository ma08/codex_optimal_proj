

#Solution 1

#input number
n = int(input())

#initialize count variable
count = 0

#loop through numbers from 1 to n
for i in range(1, n + 1):
    #convert number to string
    s = str(i)
    #loop through string
    for j in range(len(s)):
        #if number is divisible by 3, add 1 to count
        if int(s[j]) % 3 == 0:
            count += 1

#print count
print(count)

#Solution 2

#input number
n = int(input())

#initialize count
count = 0

#loop through list
for i in range(len(s)):
    #if the number is divisible by 3, add 1 to count
    if int(s[i]) % 3 == 0:
        count += 1

#print count
print(count)
