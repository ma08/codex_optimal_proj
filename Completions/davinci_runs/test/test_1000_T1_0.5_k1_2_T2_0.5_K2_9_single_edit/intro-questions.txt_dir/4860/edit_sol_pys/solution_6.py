
import sys

def main():
    n = int(sys.stdin.readline().strip())
    recited = [int(sys.stdin.readline().strip()) for i in range(n)]
    missing = []
    for i in range(1, recited[-1] + 1):
        if i not in recited:
            missing.append(i)
    if len(missing) > 0:
        for m in missing:
            print(m)
    else:
        print("good job")

if __name__ == "__main__":
    main()
