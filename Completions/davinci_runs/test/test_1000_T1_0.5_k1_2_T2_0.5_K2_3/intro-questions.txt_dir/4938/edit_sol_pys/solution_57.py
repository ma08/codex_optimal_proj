


def max_people(queue, max_difference):
    w = 0
    m = 0
    max_people = 0
    for person in queue:
        if person == 'W':
            w += 1
        if person == 'M':
            m += 1
        if abs(w - m) > max_difference:
            break
        max_people += 1
    return max_people


def main():
    max_difference = int(input())
    queue = input()
    print(max_people(queue, max_difference))


main()
