

#Solution

#input
s = input().strip()

#convert to list
s = list(map(int, s))

#initialize count
count = 0

#loop through list
for i in range(len(s)):
    #if the number is divisible by 3, add 1 to count
    if s[i] % 3 == 0:
        count += 1

#print count
print(count)
