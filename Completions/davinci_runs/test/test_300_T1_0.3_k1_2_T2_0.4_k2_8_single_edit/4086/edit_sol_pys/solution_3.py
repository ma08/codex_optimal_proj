
def main():
    n = int(input())
    a = list(map(int, input().split()))

    a_set = list(set(a))
    a_dict = {i: a.count(i) for i in a_set}

    a_set.sort(key=lambda x: a_dict[x], reverse=True)
    print(len(a_set))
    print(' '.join(map(str, a_set)))

if __name__ == '__main__':
    main()
