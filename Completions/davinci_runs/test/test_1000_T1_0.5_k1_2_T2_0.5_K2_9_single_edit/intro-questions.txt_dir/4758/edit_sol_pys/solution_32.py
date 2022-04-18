import sys

def main():
    n, t, m = [int(i) for i in sys.stdin.readline().split()] #n,t,m is the input
    print(n * t * m) #print the result

if __name__ == "__main__":
    main()
