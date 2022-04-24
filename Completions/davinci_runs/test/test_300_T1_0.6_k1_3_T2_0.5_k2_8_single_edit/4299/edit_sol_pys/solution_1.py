n = int(input())

if n%10==2 or n%10==4 or n%10==5 or n%10==7 or n%10==9:
    print("hon")
elif n%10==0 or n%10==1 or n%10==6 or n%10==8:
    print("pon")
elif n%10==3:
    print("bon")
