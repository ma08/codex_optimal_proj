
import sys

def main():
    lines = sys.stdin.readlines()
    num_cases = int(lines[0])
    for case in range(num_cases):
        num_packages = int(lines[2 * case + 1])
        packages = [tuple(map(int, lines[2 * case + 2 + j].split())) for j in range(num_packages)]
        print("YES" if is_possible(packages) else "NO")

def is_possible(packages):
    packages.sort()
    for index in range(len(packages)):
        if packages[index][0] < index or packages[index][1] < index:
            return False
    return True

if __name__ == '__main__':
    main()
