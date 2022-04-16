

def main():
    n, d = map(int, input().split())  # number of days and target day
    ds = list(map(int, input().split()))  # list of days
    ds.append(d)  # add target day to list
    count = 0  # number of days earlier than target
    for i in range(len(ds)):  # iterate through days
        if ds[i] > ds[-1]:  # if day is earlier than target
            count += 1  # increment count by 1
        else:
            break
    if count == 0:
        print("It had never snowed this early!")
    else:
        print("It hadn't snowed this early in {} years!".format(count))

if __name__ == "__main__":
    main()
