
import sys

def main(r):
    return 3 * r**2

if __name__ == '__main__':
    r = int(sys.stdin.readline().strip())
    print(main(r))
