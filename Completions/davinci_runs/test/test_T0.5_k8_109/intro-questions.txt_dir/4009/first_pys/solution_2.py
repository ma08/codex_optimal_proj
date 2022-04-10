

n,x,y = map(int,input().split())
s = input()

if s[:x] == '1' + '0'*(x-1):
    print(0)
else:
    if s[:x] == '0'*x:
        print(1)
    else:
        if s[:y] == '1' + '0'*(y-1):
            print(x-y)
        else:
            print(x-y+1)