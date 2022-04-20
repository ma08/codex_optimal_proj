

def main():
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))
    left = [i for i in a if i < x]
    right = [i for i in a if i > x]
    print(min(len(left), len(right)))

if __name__ == '__main__':
    main()
