
def main():
    max_difference = int(input())
    queue = input()
    max_people = 0
    w = 0
    m = 0
    for person in queue:
        if person == 'W':
            w += 1
        if person == 'M':
            m += 1
        if abs(w - m) > max_difference:
            break
        max_people += 1
    print(max_people)

main()
