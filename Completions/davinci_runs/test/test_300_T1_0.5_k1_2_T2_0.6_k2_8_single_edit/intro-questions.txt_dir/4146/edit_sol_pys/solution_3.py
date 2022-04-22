
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_set = set(a)
    print(((sum(a_set) * n) - sum(a)) // (n - 1))




if __name__ == '__main__':
    main()
