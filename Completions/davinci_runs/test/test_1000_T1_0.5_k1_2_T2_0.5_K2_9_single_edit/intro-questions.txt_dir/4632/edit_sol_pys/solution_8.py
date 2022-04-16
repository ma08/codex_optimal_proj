import sys

def main():
    num_cases = int(sys.stdin.readline())
    for i in range(num_cases):
        num_packages = int(sys.stdin.readline())
        packages = [tuple(map(int, sys.stdin.readline().split())) for j in range(num_packages)]
        print("YES" if is_possible(packages) else "NO")

def is_possible(packages):
    packages.sort()
    for i in range(len(packages)):
        if packages[i][0] < i or packages[i][1] < i:
            return False
    return True

if __name__ == '__main__':
    main()
