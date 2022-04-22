


n = int(input())
lst = []
for i in range(n):
    lst.append(input())

for i in lst:
    if len(i) == len(set(i)) and len(set(i)) == ord(max(i)) - ord(min(i)) + 1:
        print("Yes")
    else:
        print("No")
