
def main():
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]  # list comprehension
    print(sum(1 for x in a if x <= k))

if __name__ == "__main__":
    main()
