
import os
import re
import sys

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        path = sys.stdin.readline().strip()
        if isValid(path):
            print("YES")
        else:
            print("NO")

def isValid(path):
    if not path.startswith('/'):
        return False
    if '//' in path:
        return False
    path = path.split('/')
    for i in path:
        if not isValidFileName(i):
            return False
    return True

def isValidFileName(filename):
    if len(filename) > 255:
        return False
    if filename.startswith('.') or filename.endswith('.') or filename.endswith(' '):
        return False
    illegalChars = re.compile(r'[\\/:*?"<>|]')
    if illegalChars.search(filename):
        return False
    return True

if __name__ == '__main__':
    main()
