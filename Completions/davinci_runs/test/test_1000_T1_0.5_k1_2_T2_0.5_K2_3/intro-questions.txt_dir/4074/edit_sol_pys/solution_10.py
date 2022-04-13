
def find(n):
    s=str(n)
    c=0
    for i in s:
        if i=='4' or i=='7':
            c+=1
    return c

test=int(input())
for i in range(test):
    n=int(input())
    print(find(n))
