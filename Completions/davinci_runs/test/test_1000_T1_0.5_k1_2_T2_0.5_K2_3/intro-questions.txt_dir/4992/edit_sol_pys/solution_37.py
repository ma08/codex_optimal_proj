

import sys

import sys

def main():
    n = int(sys.stdin.readline())  # number of students
    rooms = [int(x) for x in sys.stdin.readline().split()]  # capacity of each room

    # If the total number of students is less than the number of rooms,
    # then it is impossible to redistribute the exams safely
    if sum(rooms) < n:  # if the total capacity of the rooms is not enough for the students
        print("impossible")
        return

    # We can simply use the greedy approach and choose the room with
    # the most students first. This is always a safe order.
    rooms = sorted(enumerate(rooms), key=lambda x: x[1], reverse=True)  # sort the rooms by their capacity
    print(" ".join([str(x[0] + 1) for x in rooms]))

if __name__ == "__main__":
    main()
