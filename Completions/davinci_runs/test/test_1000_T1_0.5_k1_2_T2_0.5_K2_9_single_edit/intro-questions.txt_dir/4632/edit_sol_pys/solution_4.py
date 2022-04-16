import sys

def main():
    lines = sys.stdin.readlines()
    num_cases = int(lines[0])
    for case_index in range(num_cases):
        num_packages = int(lines[2 * case_index + 1])
        packages = [tuple(map(int, lines[2 * case_index + 2 + j].split())) for j in range(num_packages)]
        print("YES" if is_possible(packages) else "NO")

def is_possible(packages):
    packages.sort()
    for package_index in range(len(packages)):
        if packages[package_index][0] < package_index or packages[package_index][1] < package_index:
            return False
    return True

if __name__ == '__main__':
    main()
