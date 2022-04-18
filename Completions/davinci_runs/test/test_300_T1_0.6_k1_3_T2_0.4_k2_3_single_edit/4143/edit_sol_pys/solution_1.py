

n = int(input("Enter the number of people in the queue: "))
a = int(input("Enter the number of time a cashier takes to serve a customer: "))
b = int(input("Enter the number of time a cashier takes to serve a customer: "))
c = int(input("Enter the number of time a cashier takes to serve a customer: "))
d = int(input("Enter the number of time a cashier takes to serve a customer: "))
e = int(input("Enter the number of time a cashier takes to serve a customer: "))

if n>a and n>b and n>c and n>d and n>e:
    time = 0
    while n:
        if n>a:
            n-=a
        else:
            n=0
        time+=1
        if n>b:
            n-=b
        else:
            n=0
        time+=1
        if n>c:
            n-=c
        else:
            n=0
        time+=1
        if n>d:
            n-=d
        else:
            n=0
        time+=1
        if n>e:
            n-=e
        else:
            n=0
        time+=1

    print(time)
else:
    print("Enter the correct number of people in the queue!")
