

a, b, x = map(int, input().split())
if x >= a+b:
    print("0"*a + "1"*b)
elif x <= a:
    print("0"*(a-x) + "1"*b + "0"*x)
else:
    print("0"*a + "1"*(b-x+a) + "0"*x)
