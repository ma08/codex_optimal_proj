

def main():
    line = list(map(int, input().split()))[1:]
    print(1, end=" ")
    for i in range(len(line)):
        print(i+line[i], end=" ")

main()
