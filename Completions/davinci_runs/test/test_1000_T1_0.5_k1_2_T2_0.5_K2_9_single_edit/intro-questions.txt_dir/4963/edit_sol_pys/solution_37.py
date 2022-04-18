

def main():
    line = list(map(int, input().split()))[1:]
    # print(line)
    print(1, end=" ")
    for i in range(1, len(line)):
        print(i+1+line[i], end=" ")

main()
