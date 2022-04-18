

import sys

def main():
    nums = sys.stdin.readline().split()
    a = int(nums[0])
    b = int(nums[1])
    c = int(nums[2])

    if a + b == c:
        print(str(a) + "+" + str(b) + "=" + str(c))
    elif a - b == c:
        print(str(a) + "-" + str(b) + "=" + str(c))
    elif a * b == c:
        print(str(a) + "*" + str(b) + "=" + str(c))
    elif a == b + c:
        print(str(a) + "=" + str(b) + "+" + str(c))
    elif a == b - c:
        print(str(a) + "=" + str(b) + "-" + str(c))
    elif a == b * c:
        print(str(a) + "=" + str(b) + "*" + str(c))
    else:
        print(str(a) + "=" + str(b) + "/" + str(c))

if __name__ == '__main__':
    main()
