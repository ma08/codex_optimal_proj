

def main():
    n, d = map(int, input().split())
    ds = list(map(int, input().split()))
    ds.append(0)
    count = 0
    for i in range(len(ds)):
        if ds[i] > ds[-1]:
            count += 1
        else:
            break
    if count == 0:
        print("It had never snowed this early!")
    else:
        print("It hadn't snowed this early in {} year{}!".format(count, "" if count == 1 else "s"))

if __name__ == "__main__":
    main()
