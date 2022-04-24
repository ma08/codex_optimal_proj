
def main():
    n = int(input())

    soft = []
    hard = []

    for i in range(n):
        a, b = input().split()
        if b == "hard":
            hard.append(int(a))
        elif b == "soft":
            soft.append(int(a))

    soft = sorted(soft, reverse=True)
    hard = sorted(hard, reverse=True)

    if len(soft) > len(hard):
        print(len(hard))
    else:
        print(len(soft))

if __name__ == "__main__":
    main()
