
def main():
    n = int(input())
    recited = []
    for _ in range(n):
        recited.append(int(input()))
    recited.sort()
    for i in range(1, 201):
        if i not in recited:
            print(i)

if __name__ == "__main__":
    main()
