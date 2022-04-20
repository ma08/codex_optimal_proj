

import math

def main():
    k = int(input())
    n = k
    count = 1
    while n < 10**6:
        if n % k == 0:
            print(count)
            break
        count += 1
        n = int(str(n) + "7")
    else:
        print(-1)


if __name__ == "__main__":
    main()