

a,b,c = map(int,input().split())#a,b,cに対して入力を代入
k = int(input())#kに対して入力を代入

if k%2 == 1:#奇数のとき
    print(a*2**k+b*2**(k//2)+c*2**(k//3))#a*2^k+b*2^(k//2)+c*2^(k//3)を出力する
else:
    print(a*2**k+b*2**(k//2)+c*2**(k//3))#a*2^k+b*2^(k//2)+c*2^(k//3)を出力する
