

n = int(input())
lst = []
for i in range(n):
    lst.append(input())

for i in lst:  # for every word
    if len(i) == len(set(i)):  # if the length of the word is equal to the length of the set of the word
        print("Yes")
    else:
        print("No")
