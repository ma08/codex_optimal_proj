import sys



def main():
    # get input from stdin
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    b = [int(x) for x in sys.stdin.readline().split()]

    # print result to stdout
    sys.stdout.write("{} {}\n".format(min_wins, max_wins))

if __name__ == "__main__":
    main()
