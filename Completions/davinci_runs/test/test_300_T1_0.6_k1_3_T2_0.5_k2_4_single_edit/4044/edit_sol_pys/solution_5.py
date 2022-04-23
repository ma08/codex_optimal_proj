

a, b, x = map(int, raw_input().split())
if (a - x) < b and (b - x) < a:
    zeros = a - (x - b)
    print "1" * (x - zeros) + "0" * zeros + "1" * b
