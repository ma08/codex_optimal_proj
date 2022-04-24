
import sys

n = int(sys.stdin.readline())

if n % 25 == 0:
    print(0)
else:
    for i in range(1, len(str(n))):
        for j in range(i):
            if int(str(n)[j:j + 1] + str(n)[i:i + 1]) % 25 == 0:
                print(1)
                break
        else:
            continue
        break
    else:
        print(0)
