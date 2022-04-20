

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a_dict = {i: a.count(i) for i in set(a)}
    a_list = [i for i in a_dict]

    a_list.sort(key=lambda x: a_dict[x], reverse=True) 

    print(len(a_list))
    print(' '.join(map(str, a_list)))

if __name__ == '__main__':
    main()
