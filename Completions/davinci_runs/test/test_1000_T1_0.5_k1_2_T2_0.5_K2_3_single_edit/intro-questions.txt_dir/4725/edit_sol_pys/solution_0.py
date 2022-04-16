
import sys

def main():
    for line in sys.stdin:
        res = 0
        count = [0]*26
        for i in line:
            count[ord(i)-ord('a')] += 1
        for i in count:
            if i > 2:
                res += i-2
        print(res)

if __name__ == '__main__':
    main()
