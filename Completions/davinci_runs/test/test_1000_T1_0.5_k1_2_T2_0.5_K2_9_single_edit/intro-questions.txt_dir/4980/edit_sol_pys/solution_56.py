

import sys

def main():
    n = int(input().strip())
    count = 0
    for i in range(n):
        s = input().strip()
        s = s.lower()
        if 'pink' in s or 'rose' in s:
            count += 1
    if count == 0:
        print('I must watch Star Wars with my daughter')
    else:
        print(count)

if __name__ == "__main__":
    main()
