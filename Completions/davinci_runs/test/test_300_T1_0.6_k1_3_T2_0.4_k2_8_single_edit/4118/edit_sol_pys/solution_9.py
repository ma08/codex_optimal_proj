

a,b = map(int,input().split())

if a==1 or b==1:
    print(1)
elif a==2 and b==2:
    print(4)
elif a==2 and b in [3,4,5,6,8,9]:
    print(6)
elif a==2 and b==7:
    print(-1)
elif a==3 and b==3:
    print(9)
elif a==3 and b in [2,4,5,6,7,8,9]:
    print(6)
elif a==4 and b==4:
    print(6)
elif a==4 and b in [2,3,5,6,7,8,9]:
    print(8)
elif a==5 and b==5:
    print(5)
elif a==5 and b in [2,3,4,6,7,8,9]:
    print(-1)
elif a==6 and b==6:
    print(6)
elif a==6 and b in [2,3,4,5]:
    print(-1)
elif a==7 and b==7:
    print(9)
elif a==7 and b in [2,3,4,5,6,8,9]:
    print(-1)
elif a==8 and b==8:
    print(4)
elif a==8 and b in [2,3,4,5,6,7,9]:
    print(2)
elif a==9 and b==9:
    print(1)
elif a==9 and b in [2,3,4,5,6,7,8]:
    print(-1)
