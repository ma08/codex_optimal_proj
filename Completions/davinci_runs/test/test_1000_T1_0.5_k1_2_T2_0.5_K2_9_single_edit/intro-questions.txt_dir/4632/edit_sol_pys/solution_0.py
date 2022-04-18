

import sys

def main():
    lines = sys.stdin.readlines()
    num_cases = int(lines[0])
    for i in range(num_cases):
        num_packages = int(lines[2 * i + 1])
        packages = [tuple(map(int, lines[2 * i + 2 + j].split())) for j in range(num_packages)]        
        print("YES" if is_possible(packages) else "NO")        

def is_possible(packages):
    packages.sort()        
    for i in range(len(packages)):
        if packages[i][0] < i or packages[i][1] < i:            
            return False        
    return True        

if __name__ == '__main__':
    main()
