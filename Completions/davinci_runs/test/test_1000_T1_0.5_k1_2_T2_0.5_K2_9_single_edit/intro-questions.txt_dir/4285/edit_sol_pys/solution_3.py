
import sys

def main():
    # read number of strings
    n = int(sys.stdin.readline().strip())

    # read strings
    ss = [sys.stdin.readline().strip() for _ in range(n)]

    # count number of strings that contain 's'
    count = 0
    for s in ss:
        if 's' in s:
            count += 1

    # print number of strings that contain 's'
    print(count)    

if __name__ == '__main__':
    main()
