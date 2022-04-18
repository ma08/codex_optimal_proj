

def main():
    n = int(input())  # number of files

    soft = []
    hard = []

    for i in range(n):
        a, b = input().split()  # name of file and type
        if b == "soft":  # soft link
            soft.append(a)
        else:
            hard.append(a)

    soft.sort()
    hard.sort()

    if len(soft) > len(hard):
        print(len(hard))
    else:
        print(len(soft))

if __name__ == "__main__":
    main()
