from collections import defaultdict

def main():
    n = int(input())
    d = defaultdict(int)
    for i in range(n):
        s = input()
        d[s] += 1
    print(max(d.values()))

if __name__ == "__main__":
    main()
