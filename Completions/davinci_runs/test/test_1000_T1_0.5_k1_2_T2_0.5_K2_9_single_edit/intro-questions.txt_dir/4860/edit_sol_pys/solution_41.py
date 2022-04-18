
def main():
    n = int(input())
    recited = []
    for _ in range(n):
        recited.append(int(input()))
    recited.sort()
    for i in range(n):
        if i == 0:
            if recited[i] != 1:
                print(1)
        elif i == n-1:
            if recited[i] != 200:
                print(recited[i]+1)
        else:
            for j in range(recited[i-1]+1, recited[i]):
                print(j)

if __name__ == "__main__":
    main()
