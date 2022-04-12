
#!/usr/bin/env python3
import sys

class Room:
    def __init__(self, id, num_students):
        self.id = id
        self.num_students = num_students
        self.num_exams = 0
        self.num_exams_needed = 0

    def __str__(self):
        return 'Room %d: %d students, %d exams' % (self.id, self.num_students, self.num_exams)

    def __repr__(self):
        return self.__str__()

    def add_exam(self, num_exams):
        self.num_exams += num_exams

    def add_exam_needed(self, num_exams_needed):
        self.num_exams_needed += num_exams_needed

    def get_num_exams_needed(self):
        return self.num_exams_needed

    def get_num_exams(self):
        return self.num_exams

    def get_id(self):
        return self.id

def get_num_exams_needed(rooms):
    num_exams_needed = 0
    for room in rooms:
        num_exams_needed += room.get_num_exams_needed()
    return num_exams_needed

def get_num_exams(rooms):
    num_exams = 0
    for room in rooms:
        num_exams += room.get_num_exams()
    return num_exams

def dfs(rooms, visited, order):
    if len(visited) == len(rooms):
        if get_num_exams_needed(rooms) == get_num_exams(rooms):
            return order
        else:
            return None
    for i, room in enumerate(rooms):
        if i in visited:
            continue
        visited.add(i)
        order.append(room.get_id())
        for r in rooms:
            r.add_exam_needed(r.get_num_students())
        for r in rooms:
            r.add_exam(r.get_num_students())
        if room.get_num_exams_needed() > room.get_num_exams():
            break
        for r in rooms:
            r.add_exam_needed(-r.get_num_students())
            r.add_exam(-r.get_num_students())
        result = dfs(rooms, visited, order)
        if result:
            return result
        order.pop()
        visited.remove(i)
    return None

def main():
    num_rooms = int(sys.stdin.readline().strip())
    rooms = []
    for i in range(num_rooms):
        num_students = int(sys.stdin.readline().strip())
        rooms.append(Room(i + 1, num_students))
    order = dfs(rooms, set(), [])
    if order:
        print(' '.join(map(str, order)))
    else:
        print('impossible')

if __name__ == '__main__':
    main()
