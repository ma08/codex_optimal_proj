
import sys

def main():
    lines = sys.stdin.readlines()
    num_cases = int(lines[0]) // 2
    for i in range(1, num_cases + 1):
        num_packages = int(lines[2 * i + 1])
        packages = [tuple(map(int, lines[2 * i + 2 + j].split())) for j in range(1, num_packages + 1)]
        print("YES" if is_possible(packages) else "NO")

    print(packages)
def is_possible(packages):
    packages.sort()
    for i in range(len(packages)):
        if packages[i][0] < i or packages[i][1] < i + 1:
            return False
    return True

if __name__ == '__main__':
    main()
