

def main():
    n = int(input())

    soft = []
    hard = []

    for _ in range(n):
        a, b = input().split()
        if b == "soft":
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
