import sys

def main():
    data = sys.stdin.read().splitlines()
    for line in data:
        if len(line) == 1:
            print(1)
            continue
        b_count = 0
        w_count = 0
        for i in range(len(line)):
            if line[i] == 'B':
                b_count += 1
            else:
                w_count += 1
        if b_count == w_count:
            print(1)
            continue
        if b_count > w_count:
            if b_count - w_count == 1:
                print(1)
                continue
        if w_count > b_count:
            if w_count - b_count == 1:
                print(1)
                continue
        print(0)

if __name__ == "__main__":
    main()
