

def main():
    n = int(input())
    recited = []
    for _ in range(n):
        recited.append(int(input()))
    recited.sort()
    if recited[0] != 1:
        print(1)
    for i in range(n-1):
        if recited[i+1] - recited[i] != 1:
            for j in range(recited[i]+1, recited[i+1]+1):
                print(j)
    if recited[-1] != 200:
        print(200)

if __name__ == "__main__":
    main()
