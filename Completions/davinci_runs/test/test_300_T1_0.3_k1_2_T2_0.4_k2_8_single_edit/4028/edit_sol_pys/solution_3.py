
import sys

def get_input():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    return n, s.split()

def solve(n, s_list):
    return len(s_list)

def main():
    n, s = get_input()
    print(solve(n, s))

if __name__ == '__main__':
    main()
