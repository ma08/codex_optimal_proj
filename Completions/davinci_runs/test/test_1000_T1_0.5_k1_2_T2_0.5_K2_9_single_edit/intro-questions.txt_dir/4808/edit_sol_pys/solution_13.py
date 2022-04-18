
def main():
    n, d = map(int, input().split())
    ds = list(map(int, input().split()))
    ds.append(0)
    count = 0
    for i in range(len(ds)-1):
        if ds[i] > ds[-2]:
            count += 1
        else:
            break
    if count == 0:
        print("It had never snowed this early!")
    else:
        print("It hadn't snowed this early in {} years!".format(count))

if __name__ == "__main__":
    main()
