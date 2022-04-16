
def main():
    n = int(input())
    rolls = list(map(int, input().split()))
    for i in range(1, 7):
        if rolls.count(i) == 1:
            print(rolls.index(i) + 1)
            break
    else: print("none")

if __name__ == "__main__":
    main()
