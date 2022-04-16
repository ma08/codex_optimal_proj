

# cook your dish here
def find(n):
    count=0
    for i in range(n):
        count+=1
        if count==n:
            return i
        else:
            count+=i

test=int(input())
for i in range(test):
    n=int(input())
    print(find(n))
