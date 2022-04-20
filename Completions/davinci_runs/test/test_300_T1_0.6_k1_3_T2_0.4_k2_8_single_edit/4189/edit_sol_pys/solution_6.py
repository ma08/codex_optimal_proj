

def main():
    n = int(input()) # number of files

    soft = []
    hard = []

    for i in range(n):
        a, b = input().split() # a is the name of the file, b is the type of file
        if b == "soft":
            soft.append(a)
        else:
            hard.append(a)

    soft.sort() # sort the files by name
    hard.sort() # sort the files by name

    if len(soft) > len(hard):
        print(len(hard))
    else:
        print(len(soft))

if __name__ == "__main__":
    main()
