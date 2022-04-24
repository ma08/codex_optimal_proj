

def main():
    n = int(input())

    hard = 0
    soft = 0

    for i in range(n):
        a, b = input().split()
        if b == "soft":
            soft += 1
        else:
            hard += 1
    print(min(soft, hard) * 2)

if __name__ == "__main__":
    main()
