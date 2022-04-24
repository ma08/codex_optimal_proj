

a,b,c,k = map(int,input().split()) #入力

if k <= a: #条件分岐
    print(k)
elif k <= a+b:
    print(a)
else:
    print(a-(k-a-b))
