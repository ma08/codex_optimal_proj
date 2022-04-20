

import sys

def main():
    input = sys.stdin.readline()
    # input = "0011"
    input = input.replace("\n", "")
    input = list(input)

    # print(input)

    count = 0
    for i in range(len(input)):
        if input[i] == '0':
            count += 1
        else:
            break

    # print(count)

    ans = count
    for i in range(count, len(input)):
        if input[i] == '1':
            ans += 1
        else:
            break

    # print(ans)

    print(ans)

if __name__ == '__main__':
    main()