

import math
#AC

m, n, t = map(int, input().split())

if n > m:
    print("TLE")
else:
    if t == 1:
        print("AC")
    elif t == 2:
        if 2**n > m:
            print("TLE")
        else:
            print("AC")
    elif t == 3:
        if n**4 > m:
            print("TLE")
        else:
            print("AC")
    elif t == 4:
        if n**3 > m:
            print("TLE")
        else:
            print("AC")
    elif t == 5:
        if n**2 > m:
            print("TLE")
        else:
            print("AC")
    elif t == 6:
        if n*(math.log(n)/math.log(2)) > m:
            print("TLE")
        else:
            print("AC")
    elif t == 7:
        print("TLE")
    else:
        print("AC")
