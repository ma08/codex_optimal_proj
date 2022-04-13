


def main():
    people, days = map(int, input().split())
    people_names = []
    for _ in range(people):
        people_names.append(input())
    people_names_set = set(people_names)
    if len(people_names_set) < people:
        print('paradox avoided')
        return
    for i in range(days):
        if people_names_set:
            if people_names[i] in people_names_set:
                people_names_set.remove(people_names[i])
                if not people_names_set:
                    print(i+1)
                    return


if __name__ == '__main__':
    main()
