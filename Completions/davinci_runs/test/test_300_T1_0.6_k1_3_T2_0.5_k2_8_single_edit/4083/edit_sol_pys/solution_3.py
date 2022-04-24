
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_num_operations(n, a))



def min_num_operations(n, a):
    return n - len(set(a))


if __name__ == '__main__':
    main()
