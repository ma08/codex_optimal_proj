
#
n = input()

if len(n)==1 and n=="9":
    print("Yes")
elif len(n)==1:
    print("No")
else:
    if sum([int(i) for i in n])%9==0:
        print("Yes")
    else:
        print("No")
