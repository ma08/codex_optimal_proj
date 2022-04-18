import sys

def main():
    n = int(sys.stdin.readline().strip())
    recited = [int(sys.stdin.readline().strip()) for _ in range(n)] # recite
    missing = []
    for i in range(1, recited[-1] + 1): # recite
        if i not in recited:
            missing.append(i)
    if len(missing) > 0:
        for m in missing:
            print(m)
    else:
        print("good job")

if __name__ == "__main__":
    main()
