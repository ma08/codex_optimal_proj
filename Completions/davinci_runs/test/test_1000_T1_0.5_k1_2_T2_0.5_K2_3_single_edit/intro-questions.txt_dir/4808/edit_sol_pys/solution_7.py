

def main():
    n = int(input())
    days = list(map(int, input().split()))
    for i in range(n):
        if days[i] <= days[-1]: break
    print("It hadn't snowed this early in {} years!".format(i))




if __name__ == "__main__":
    main()
