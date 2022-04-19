

def min_changes(s, t):
    count = 0
    for x, y in zip(s, t):
        if x != y:
            count += 1
    return count

def main():
    s = input()
    t = input()
    print(min_changes(s, t))

if __name__ == '__main__':
    main()
