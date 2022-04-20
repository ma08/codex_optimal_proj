
import sys

def main():
    k = int(sys.stdin.readline().strip()) # read the input
    i = 1
    while True:
        if not (7 * (10 ** i) - 7) % k: # if the remainder is zero
            print(i + 1) # print i + 1
            break # break the loop
        i += 1

if __name__ == '__main__':
    main()
