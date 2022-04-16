

def main():
    input()
    line = list(map(int, input().split()))
    print(line)
    print(1, end=" ")
    for i in range(len(line)):
        print(i+2+line[i], end=" ")

main()
