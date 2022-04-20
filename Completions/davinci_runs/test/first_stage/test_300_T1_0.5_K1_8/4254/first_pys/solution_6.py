

def main():
    # get input
    sheep, wolves = map(int, input().split())

    # check and output
    if wolves >= sheep:
        print("unsafe")
    else:
        print("safe")

if __name__ == "__main__":
    main()