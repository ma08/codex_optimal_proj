

def main():
    n = int(input())  # number of people
    a = int(input())  # time to finish a task
    b = int(input())  # time to finish b task
    c = int(input())  # time to finish c task
    d = int(input())  # time to finish d task
    e = int(input())  # time to finish e task

    l = [a, b, c, d, e]  # list of time to finish tasks
    l.sort()  # sort the list

    if n <= l[0]:  # if number of people <= time to finish a task
        print(1)
    else:  # if number of people > time to finish a task
        print(2)

if __name__ == '__main__':
    main()
