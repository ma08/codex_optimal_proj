

def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    for i in range(k, n):
        if a_list[i - k] < a_list[i]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
