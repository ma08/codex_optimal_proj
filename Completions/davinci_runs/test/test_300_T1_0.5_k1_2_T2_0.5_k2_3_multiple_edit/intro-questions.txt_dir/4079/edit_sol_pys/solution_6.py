
n = int(input())
lst = []
for i in range(n):
    lst.append(input())
    if len(lst[i]) == len(set(lst[i])):
        print('Yes')
        else:
            print('No')
