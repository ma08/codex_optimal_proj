

def main():
    n = int(input()) # number of files

    soft = []
    hard = []

    for i in range(n):
        a, b = input().split() # a: file name, b: file type
        if b == "soft":
            soft.append(a)
        else:
            hard.append(a)

    soft.sort() # sort in ascending order
    hard.sort() # sort in ascending order

    if len(soft) > len(hard):
        print(len(hard))
    else:
        print(len(soft))

if __name__ == "__main__":
    main()
