import sys

def main():
    n = int(sys.stdin.readline().strip())  # read the number of keys
    key_set = set()
    for i in range(n):
        key = sys.stdin.readline().strip().lower().replace("-", " ")  # read the key
        key_set.add(key)
    print(len(key_set))

if __name__ == "__main__":
    main()
