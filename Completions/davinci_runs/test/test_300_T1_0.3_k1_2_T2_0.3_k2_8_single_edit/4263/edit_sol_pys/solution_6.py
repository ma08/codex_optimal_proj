import sys

def main():
    S = sys.stdin.readline().rstrip()
    print(len(max(S.split('ACGT'), key=len)))

if __name__ == '__main__':
    main()
