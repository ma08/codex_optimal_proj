

def main():
    # read input
    a = [int(x) for x in input().split()]
    # compute answer
    ans = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            ans += a[i]*a[j]
    # print answer
    print(ans)

if __name__ == '__main__':
    main()
