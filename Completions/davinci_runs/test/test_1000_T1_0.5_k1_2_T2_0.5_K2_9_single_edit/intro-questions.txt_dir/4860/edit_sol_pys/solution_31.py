import sys

def main():
    n = int(sys.stdin.readline().strip())
    recited = [int(sys.stdin.readline().strip()) for _ in range(n)]
    for i in range(1, recited[-1]+1):
        if i in recited:
            continue
        print(i)
    if len(missing) == 0:
        print("good job")

if __name__ == "__main__":
    main()
