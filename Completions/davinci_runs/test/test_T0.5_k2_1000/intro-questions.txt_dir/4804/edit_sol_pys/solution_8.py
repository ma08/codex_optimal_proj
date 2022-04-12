#!/usr/bin/env python3



def main():
    S = int(input())
    print(S, ":", sep="")
    for i in range(2, S//2 + 1):
        if S % i == 0:
            j = S // i
            if i >= j:
                print("{},{}".format(i,j))

if __name__ == "__main__":
    main()
