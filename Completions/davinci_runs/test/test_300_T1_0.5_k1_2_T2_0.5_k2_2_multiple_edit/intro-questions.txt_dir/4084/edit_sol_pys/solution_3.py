a,b = map(int,input().split())

if a % b == 0:
    print(0) # 余りがない場合は0
else:
    print(min(n,a))
