

def main():
    n = int(input())
    read = []
    for _ in range(n):
        read.append(int(input()))
    read.sort()
    if read[0] != 0:
        print(0)
    for i in range(n-1):
        if read[i+1] - read[i] != 1:
            print(read[i]+1)
    if read[-1] != 99:
        print(read[-1])

if __name__ == "__main__":
    main()
