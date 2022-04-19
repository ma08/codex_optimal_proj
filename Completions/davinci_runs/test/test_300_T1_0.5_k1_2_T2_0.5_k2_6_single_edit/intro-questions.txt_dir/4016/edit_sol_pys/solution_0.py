

def main():
    n, k = map(int, input().split())
    t = input()
    print(t*(k//n) + t[:k%n]) #k%n is the remainder of k//n

if __name__ == "__main__":
    main()
