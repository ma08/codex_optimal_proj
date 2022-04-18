
import sys

def main():
    n = int(sys.stdin.readline().strip())
    recite = [int(sys.stdin.readline().strip()) for _ in range(n)]
    missing = []
    for i in range(1, recite[-1] + 1):
        if i not in recite:
            missing.append(i)
    if len(missing) > 0:
        for m in missing:
            print(m)
    else:
        print("good job")

if __name__ == "__main__":
    main()
