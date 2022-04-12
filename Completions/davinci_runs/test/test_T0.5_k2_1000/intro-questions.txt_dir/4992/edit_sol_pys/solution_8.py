

def main():
    """
    First input is the number of rooms
    Second input is the number of students in each room
    """
    num_rooms = int(input())
    students = list(map(int, input().split()))
    # The first room will always be the last room in the sequence
    order = [num_rooms]
    # This will keep track of the number of exams in the pile
    exams = 0
    for i in range(num_rooms - 1, -1, -1):
        # If the number of exams in the pile is less than the number of students in the room, then you can't visit the room
        if exams < students[i]:
            print("impossible")
            return
        # Add the room to the sequence
        order.append(i)
        # Add the number of students in the room to the number of exams in the pile
        exams += students[i]
    # If the number of exams in the pile is not equal to the number of students in the first room, then you can't visit the room
    if exams != students[0]:
        print("impossible")
        return
    # Add the first room to the sequence
    order.append(1)
    # Print the sequence
    print(" ".join(map(str, order)))

if __name__ == "__main__":
    main()
