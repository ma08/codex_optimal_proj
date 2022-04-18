import sys

def main():
    n = int(sys.stdin.readline().strip())
    count = 0
    for i in range(n):
        s = sys.stdin.readline().strip()
        s = s.lower()
        if 'pink' in s or 'rose' in s:
            count += 1
    if count == 0:
        print('I must watch Star Wars with my daughter')
    else:
        print(count)
if __name__ == "__main__":
    main()
