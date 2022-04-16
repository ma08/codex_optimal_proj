
import sys

def main(pname):
    sys.stdin = open(pname + '.in', 'r') #redirects input to file
    sys.stdout = open(pname + '.out', 'w') #redirects output to file

    n = int(input())
    intervals = []
    for i in range(n): #inputs start and end times of each cow
        l, u = [int(j) for j in input().split()]
        intervals.append((l, u))
    intervals.sort() #sorts list by start time
    room_count = 0 #initializes room count
    curr_room = intervals[0][0]
    for i in range(n): #iterates through cows
        if intervals[i][0] <= curr_room:
            curr_room = max(curr_room, intervals[i][1]) #updates curr_room if cow is in same room
        else:
            room_count += 1 #adds to room count if cow is in a new room
            curr_room = intervals[i][1] #updates curr_room to current cow's end time
    print(room_count + 1) #prints number of rooms

if __name__ == "__main__":
    main('airconditioned')
