

def main():
    input()
    line = list(map(int, input().split()))
    # print(line)
    print(1, end=" ")
    for i in range(len(line)-1):
        print(i+3+line[i], end=" ")
    print(i+3+line[i])

main()
