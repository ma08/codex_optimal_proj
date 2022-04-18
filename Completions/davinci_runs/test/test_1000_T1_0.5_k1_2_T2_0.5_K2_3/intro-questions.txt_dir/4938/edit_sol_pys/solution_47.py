
def main():
    max_diff = int(input())
    queue = list(input())
    max_people = 0
    w = 0
    m = 0
    for i in range(len(queue)):
        if queue[i] == 'W':
            w += 1
        if queue[i] == 'M':
            m += 1
        if abs(w - m) > max_diff:
            break
        max_people += 1
    print(max_people)


if __name__ == '__main__':
    main()
