import sys

def main():
    n = int(sys.stdin.readline())
    rooms = [int(x) for x in sys.stdin.readline().split()]

    # If the total number of students is less than the number of rooms,
    # then it is impossible to redistribute the exams safely
    if sum(rooms) < n:
        print("impossible")
        return

    # We can simply use the greedy approach and choose the room with
    # the most students first. This is always a safe order
    rooms = sorted(enumerate(rooms), key=lambda x: x[1], reverse=True)
    print(" ".join([str(x[0] + 1) for x in rooms]))

if __name__ == "__main__":
    main()
