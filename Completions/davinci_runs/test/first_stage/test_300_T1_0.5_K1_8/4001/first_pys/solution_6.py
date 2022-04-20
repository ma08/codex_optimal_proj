

def main():
    n = int(input())
    divs = [int(x) for x in input().split()]
    res = []
    for i in range(n):
        if divs[i] not in res:
            res.append(divs[i])
    print(res[0], res[1])

if __name__ == "__main__":
    main()