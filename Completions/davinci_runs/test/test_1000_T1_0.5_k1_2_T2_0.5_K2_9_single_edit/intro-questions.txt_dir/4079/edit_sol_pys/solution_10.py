

n = int(input())
lst = []
for i in range(n):
    lst.append(input())

for i in range(len(lst)):
    if len(lst[i]) == len(set(lst[i])) and len(set(lst[i])) == ord(max(lst[i])) - ord(min(lst[i])) + 1:
        print("Case #%d: Yes" % (i+1))
    else: 
        print("Case #%d: No" % (i+1))
