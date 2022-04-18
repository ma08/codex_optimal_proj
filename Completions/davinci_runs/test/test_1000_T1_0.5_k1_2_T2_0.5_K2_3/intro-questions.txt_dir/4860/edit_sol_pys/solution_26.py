

def main():
    n = int(input())
    read_list = []
    for _ in range(n):
        read_list.append(int(input()))
    read_list.sort()
    if read_list[0] != 1:
        print(1)
    for i in range(n-1):
        if read_list[i+1] - read_list[i] != 1:
            for j in range(read_list[i]+1, read_list[i+1]):
                print(j)
    if read_list[-1] != 200:
        print(read_list[-1]+1)

if __name__ == "__main__":
    main()
