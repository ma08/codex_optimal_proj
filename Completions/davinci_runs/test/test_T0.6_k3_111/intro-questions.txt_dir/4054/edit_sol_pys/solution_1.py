
import sys

def main():
    f = sys.stdin
    a = list(map(int, f.readline().strip().split()))[1:]

    print(sum(a) % 3)
    
if __name__ == "__main__":
    main()
