import sys

def main():
    n = int(sys.stdin.readline().strip())
    key_set = set() # create a set
    for i in range(n):
        key = sys.stdin.readline().strip().lower().replace("-", " ") # remove "-" in keys
        key_set.add(key) # add keys to set
    print(len(key_set)) # print the number of keys

if __name__ == "__main__":
    main()
