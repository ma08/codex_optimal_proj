#decimal to binary
n=int(input())
binary=''
while n>0:
    binary=binary+str(n%2)
    n=n//2
print(binary[::-1])
