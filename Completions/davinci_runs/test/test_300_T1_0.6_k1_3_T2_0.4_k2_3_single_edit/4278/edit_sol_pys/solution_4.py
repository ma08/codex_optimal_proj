


def main():
    n = int(input())
    s_list = []
    for i in range(n):
        s_list.append(input())
    s_list.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if s_list[i] == s_list[j][:10]:
                count += 1
    print(count)


if __name__ == "__main__":
    main()
