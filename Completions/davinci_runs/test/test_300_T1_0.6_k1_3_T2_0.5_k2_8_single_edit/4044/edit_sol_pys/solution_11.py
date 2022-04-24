

a, b, x = map(int, raw_input().split())

if (a - x) >= b or b == 0:
    print "0" * x + "1" * b
elif (b - x) >= a or a == 0:
    print "1" * x + "0" * a
else:
    zeros = a - (x - b)
    print "1" * (x - zeros) + "0" * zeros + "1" * b
