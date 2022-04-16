

def main():
    input()
    line = list(map(int, input().split()))
    # print(line)
    print(1, end=" ")
    for i in range(1, len(line)):
        print(i+1+line[i], end=" ")

main()
