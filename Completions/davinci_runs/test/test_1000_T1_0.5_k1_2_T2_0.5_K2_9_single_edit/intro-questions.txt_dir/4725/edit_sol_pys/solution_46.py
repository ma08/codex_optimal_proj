import sys

def main():
    input_str = sys.stdin.readline().strip()
    if len(input_str) <= 2:
        print(0)
    else:
        chars = set()
        for i in range(len(input_str)):
            if input_str[i] not in chars:
                chars.add(input_str[i])
            if len(chars) > 2:
                print(i)
                return
        print(len(input_str))

if __name__ == '__main__':
    main()
