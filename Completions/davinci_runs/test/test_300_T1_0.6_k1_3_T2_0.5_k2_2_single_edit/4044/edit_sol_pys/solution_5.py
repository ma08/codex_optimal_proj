

a, b, x = map(int, raw_input().split())

if (b - x) >= a:
    print "1" * x + "0" * a
elif (a - x) >= b:
    print "0" * x + "1" * b
else:
    zeros = a - (x - b)
    print "1" * (x - zeros) + "0" * zeros + "1" * b
