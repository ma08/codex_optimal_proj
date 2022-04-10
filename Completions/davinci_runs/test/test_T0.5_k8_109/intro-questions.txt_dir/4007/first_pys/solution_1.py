

def main():
    n = int(input())
    f = list(map(int, input().split()))

    # If a person has a gift, they will give it to the person they have
    # If they don't have a gift, they will give it to someone who doesn't have one
    # If there is more than one person who doesn't have a gift, give it to the lowest numbered one
    for i in range(n):
        if f[i] == 0:
            for j in range(1, n+1):
                if j not in f:
                    f[i] = j
                    break

    print(*f)

if __name__ == "__main__":
    main()