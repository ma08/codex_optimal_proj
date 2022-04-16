

def main():
    n = int(input()) # number of recited numbers
    recited = []
    for _ in range(n):
        recited.append(int(input())) # list of recited numbers
    recited.sort() # sort list
    # if first recited number is not one, print one
    if recited[0] != 1:
        print(1)
    for i in range(n-1):
        if recited[i+1] - recited[i] != 1:
            for j in range(recited[i]+1, recited[i+1]):
                print(j)
    if recited[-1] != 200:
        print(recited[-1]+1)

if __name__ == "__main__":
    main()
