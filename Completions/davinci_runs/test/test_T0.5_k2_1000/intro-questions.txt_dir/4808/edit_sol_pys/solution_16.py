

def main():
    n, d = map(int, input().split())
    ds = list(map(int, input().split())) + [d]
    count = 0
    for i in range(len(ds)):
        if ds[i] > ds[-1]:
            count += 1
        else:
            break
    if count == 0:
        print("It has never snowed this early!")
    else:
        print("It hasn't snowed this early in {} years!".format(count))

if __name__ == "__main__":
    main()
