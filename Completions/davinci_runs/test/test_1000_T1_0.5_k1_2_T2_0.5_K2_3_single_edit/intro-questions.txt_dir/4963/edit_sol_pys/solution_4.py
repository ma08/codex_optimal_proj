

def main():
    input()
    line = list(map(int, input().split()))  # input line
    print(1, end=" ")  # print the first element
    for i in range(len(line)):  # print the rest of the elements
        print(i+2+line[i], end=" ")  # i+2 because the first element is 1

main()
