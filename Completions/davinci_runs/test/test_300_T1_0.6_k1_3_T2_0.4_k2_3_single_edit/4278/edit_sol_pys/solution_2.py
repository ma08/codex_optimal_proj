
def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    s_list.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if s_list[i] == s_list[j][:len(s_list[i])]:
                count += 1
                break
    print(count)


if __name__ == "__main__":
    main()
