

def main():
    n, dm = map(int, input().split())
    dn = list(map(int, input().split()))
    dn.append(dm)
    count = 0
    for i in range(n-1, -1, -1):
        if dn[i] > dn[i+1]:
            count += 1
        else:
            break
    print("It hadn't snowed this early in " + str(count) + " years!")

if __name__ == "__main__":
    main()
