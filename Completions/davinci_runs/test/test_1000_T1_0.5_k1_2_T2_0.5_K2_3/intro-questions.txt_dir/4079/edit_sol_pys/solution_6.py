

n = int(input())
lst = []
for i in range(n):
    lst.append(input())
lst2 = []
for i in lst:
    if len(i) == len(set(i)):
        lst2.append("Yes")
    elif len(i) != len(set(i)) and len(set(i)) == ord(max(i)) - ord(min(i)) + 1:
        lst2.append("Yes")
    elif len(i) != len(set(i)) and len(set(i)) != ord(max(i)) - ord(min(i)) + 1:
        lst2.append("No")
for i in lst2:
    print(i)
