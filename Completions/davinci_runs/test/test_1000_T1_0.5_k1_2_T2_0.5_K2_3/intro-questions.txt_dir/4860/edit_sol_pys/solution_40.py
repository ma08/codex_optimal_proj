

def main():
    n = int(input())
    read = []
    for _ in range(n):
        read.append(int(input()))
    read.sort()
    if read[0] != 1:
        print(1)
    for i in range(n - 1):
        if read[i + 1] - read[i] != 1:
            for j in range(read[i] + 1, read[i + 1]):
                print(j)
    if read[-1] != 200:
        print(read[-1] + 1)


if __name__ == "__main__":
    main()
