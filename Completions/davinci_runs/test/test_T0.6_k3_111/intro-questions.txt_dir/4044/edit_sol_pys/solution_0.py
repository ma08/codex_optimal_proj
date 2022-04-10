

#-------------------------------------------------------------------------------#

def main():
    a,b,x = map(int,input().split())
    s = ['0']*a+['1']*b # 初期状態
    if a+b-1-x < x:
        x = a+b-1-x
        s = s[::-1] # 反転
    
    for i in range(x):
        s[i],s[i+1] = s[i+1],s[i]
    print(''.join(s))

main()
