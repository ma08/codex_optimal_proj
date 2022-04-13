import sys
input = sys.stdin.readline
def main():
    k, s = map(int, input().rstrip().split())
    count = 0
    for x in range(k+1):
        for y in range(k+1):
            for z in range(k+1):
                if x+y+z == s:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()
