
import sys

def main():
    n = int(sys.stdin.readline().strip())
    key_set = set()
    for i in range(n):
        key = sys.stdin.readline().strip().lower().replace("-", " ")
        key_set.add(key)
    print(len(key_set))
if __name__ == "__main__":
    main()
