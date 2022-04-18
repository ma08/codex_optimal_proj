
def is_possible(slots, students, capacity, new_bottles):
    for i in range(len(slots)):
        slots[i] += new_bottles[i]
    for j in range(students):
        if sum(slots) == 0:
            return False
        for i in range(len(slots)):
            if slots[i] > 0:
                slots[i] -= 1
                break
    return True

def refill(slots, students, capacity, new_bottles):
    while not is_possible(slots, students, capacity, new_bottles):
        new_bottles[-1] -= 1
        new_bottles[-2] += 1
        if new_bottles[-1] == 0:
            new_bottles[-1] = new_bottles[-2]
            new_bottles[-2] = 0
            if new_bottles[-2] == 0:
                new_bottles[-2] = new_bottles[-3]
                new_bottles[-3] = 0
                if new_bottles[-3] == 0:
                    new_bottles[-3] = new_bottles[-4]
                    new_bottles[-4] = 0
    return new_bottles

def main():
    students, slots, capacity = map(int, input().split())
    new_bottles = list(map(int, input().split()))
    if is_possible(slots, students, capacity, new_bottles):
        print(*refill(slots, students, capacity, new_bottles))
    else:
        print("impossible")

if __name__ == '__main__':
    main()
