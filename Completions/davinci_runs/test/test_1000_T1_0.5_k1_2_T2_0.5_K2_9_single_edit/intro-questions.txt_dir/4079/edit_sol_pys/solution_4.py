

n = int(input())
lst = []
for i in range(n):
    lst.append(input())

for i in lst: # O(n)
    if len(i) == len(set(i)): # O(n)
        print("Yes")
    else:
        print("No")
