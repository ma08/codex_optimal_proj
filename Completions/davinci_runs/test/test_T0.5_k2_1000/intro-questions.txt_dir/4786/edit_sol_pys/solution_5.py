import sys

def main():
    n = int(sys.stdin.readline().strip())
    key_set = set()  # use set to remove duplicate
    for i in range(n):
        key = sys.stdin.readline().strip().lower().replace("-", " ")  # remove hyphen and convert to lower case
        key_set.add(key)
    print(len(key_set))

if __name__ == "__main__":
    main()
