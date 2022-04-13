
import sys

def main():
    for line in sys.stdin:
        res = 0
        count = [0]*26
        for i in line:
            count[ord(i)-ord('a')] += 1
        for i in count:
            if i > 1:
                res += i-1
        print(res)

main()
