import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) # map() applies a function to every item of an iterable
    # and returns a list of the results

    if sheep < wolves:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
