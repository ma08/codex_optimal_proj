def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(find(n))

def find(k):
    if k <= 3:
        return k
    return find(k - 1) + find(k - 2)

if __name__ == '__main__':
    main()
