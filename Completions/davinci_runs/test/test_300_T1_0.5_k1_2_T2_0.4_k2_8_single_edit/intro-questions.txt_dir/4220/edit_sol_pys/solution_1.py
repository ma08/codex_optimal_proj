
k = int(input())
s = input()

if len(s) <= k:  # if the length of the string is less than or equal to k
    print(s)
else:  # if the length of the string is greater than k
    print(s[:k] + "...")
