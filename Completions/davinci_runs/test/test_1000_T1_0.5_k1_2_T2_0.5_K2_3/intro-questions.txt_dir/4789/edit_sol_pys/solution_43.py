
def main():
    k = int(input())
    n = int(input())
    d = [int(input()) for _ in range(n)]
    d.sort() # O(n log n)
    print(max(d[i] - d[i - 1] for i in range(1, len(d)))) # O(n)

if __name__ == '__main__':
    main()
