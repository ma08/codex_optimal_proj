
import sys

def main():
    f = sys.stdin
    a = list(map(int, f.readline().strip().split()))

    print(sum(a) % 2)
    
if __name__ == "__main__":
    main()
