
n,a,b = map(int,input().split()) # a,bを入力

if a > b: # aとbを比較してaが大きければ入れ替える
    a,b = b,a 

if a == 0:
    print(0)
else:
    print(min(n,a))
