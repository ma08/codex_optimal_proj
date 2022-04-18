import sys


def main(argv):
    n, dm = map(int, input().split())
    d_list = list(map(int, input().split())) # d_list is a list of days

    k = 0
    while k < n and d_list[k] > dm:
        k += 1

    if k == 0:
        print("It had never snowed this early!")
    else:
        print("It hadn't snowed this early in {} years!".format(k))

if __name__ == "__main__":
    main(sys.argv)
