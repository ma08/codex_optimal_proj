
import sys

def main():
    line = sys.stdin.readline().rstrip("\r\n")
    a, b = map(int, line.split(" "))

    for i in range(1, 100):
        if int(i * 1.08) == a and int(i * 1.1) == b:  # if int(i * 1.08) == int(a) and int(i * 1.1) == int(b):
            print(i)
            sys.exit()
    print(-1)

if __name__ == '__main__':
    main()
