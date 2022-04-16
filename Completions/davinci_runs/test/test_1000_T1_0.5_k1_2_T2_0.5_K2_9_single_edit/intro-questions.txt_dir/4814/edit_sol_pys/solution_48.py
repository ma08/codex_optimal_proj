import sys

def main():
    n = int(sys.stdin.readline())
    names = []
    for i in range(n):
        names.append(sys.stdin.readline().strip())
    for i in range(1, n):
        if names[i] < names[i-1]:
            break
    else:
        print("INCREASING")
        return
    for i in range(1, n):
        if names[i] > names[i-1]:
            break
    else:
        print("DECREASING")
        return
    print("NEITHER")

if __name__ == "__main__":
    main()
