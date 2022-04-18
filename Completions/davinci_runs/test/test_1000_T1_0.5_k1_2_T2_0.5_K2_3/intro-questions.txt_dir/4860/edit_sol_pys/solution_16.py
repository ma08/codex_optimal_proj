

def main():
    n = int(input())
    recite = []
    for _ in range(n):
        recite.append(int(input()))
    recite.sort()
    if recite[0] != 1:
        print(1)
    for i in range(n - 1):
        if recite[i+1] - recite[i] != 1:
            for j in range(recite[i] + 1, recite[i + 1]):
                print(j)
    if recite[-1] != 200:
        print(recite[-1] + 1)

if __name__ == "__main__":
    main()
