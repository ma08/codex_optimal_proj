
def main():
    k = int(input())
    ans = -1
    for i in range(1,10**6+1):
        if (i*7) % k == 0:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()