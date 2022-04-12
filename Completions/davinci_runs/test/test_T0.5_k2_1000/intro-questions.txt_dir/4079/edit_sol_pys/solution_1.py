

n = int(input())
lst = []
for i in range(n):
    lst.append(input())

for i in lst:
    if len(i) == len(set(i)) and len(set(i)) == ord(max(i)) - ord(min(i)) + 1: # check if the length of the string is equal to the length of the set of the string and the length of the set of the string is equal to the difference between the maximum and minimum characters in the string
        print("Yes")
    else:
        print("No")
