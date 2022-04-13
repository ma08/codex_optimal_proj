

def main():
    n = int(input())
    recite = list()
    for _ in range(n):
        recite.append(int(input()))
    recite = sorted(recite)
    if recite[0] != 1:  # if the first number is not 1
        print(1)  # print 1
    for i in range(n-1):  # for loop through the list
        if recite[i+1] - recite[i] != 1:  # if the next number is not 1
            for j in range(recite[i]+1, recite[i+1]):  # for loop through the number
                print(j)
    if recite[-1] != 200:  # if the last number is not 200
        print(recite[-1]+1)  # print the next number

if __name__ == "__main__":
    main()
