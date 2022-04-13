
def is_possible(bottles, slots, students, capacity, new_bottles):
    for i in range(slots):
        slots += new_bottles[i]
    for j in range(students):
        if sum(slots) == 0:
            return False
        for i in range(slots):
            if slots > 0:
                slots -= 1
                break
    return True

def refill(bottles, slots, students, capacity, new_bottles):
    while not is_possible(bottles, slots, students, capacity, new_bottles):
        new_bottles[capacity - 1] -= 1
        new_bottles[capacity - 2] += 1
        if new_bottles[capacity - 1] == 0:
            new_bottles[capacity - 1] = new_bottles[capacity - 2]
            new_bottles[capacity - 2] = 0
            if new_bottles[capacity - 2] == 0:
                new_bottles[capacity - 2] = new_bottles[capacity - 3]
                new_bottles[capacity - 3] = 0
                if new_bottles[capacity - 3] == 0:
                    new_bottles[capacity - 3] = new_bottles[capacity - 4]
                    new_bottles[capacity - 4] = 0
    return new_bottles

def main():
    bottles, students, slots, capacity = map(int, input().split())
    bottles = list(map(int, input().split()))
    new_bottles = list(map(int, input().split()))
    if is_possible(bottles, slots, students, capacity, new_bottles):
        print(*refill(bottles, slots, students, capacity, new_bottles))
    else:
        print("impossible")

if __name__ == '__main__':
    main()
