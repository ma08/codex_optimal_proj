

def main():
    n = int(input())  # number of files

    soft = []
    hard = []

    for i in range(n):
        a, b = input().split()  # file name and type
        if b == "soft":  # if type is soft
            soft.append(a)  # append to soft list
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
