

def min_changes(a, b):
    count = 0
    for i in range(len(b)):
        if a[i] != b[i]:
            count += 1
    return count

def main():
    a = raw_input()
    b = raw_input()
    print(min_changes(a, b))

if __name__ == '__main__':
    main()
