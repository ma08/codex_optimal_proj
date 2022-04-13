

import sys

class Room:
    def __init__(self, id, num_students):
        self.id = id
        self.num_students = num_students
        self.num_exams = 0
        self.num_students_needed = 0

    def __str__(self):
        return 'Room %d: %d students, %d exams' % (self.id, self.num_students, self.num_exams)

    def __repr__(self):
        return self.__str__()

    def add_exam(self, num_exams):
        self.num_exams += num_exams

    def add_exam_needed(self, num_students_needed):
        self.num_students_needed += num_students_needed

    def get_num_students_needed(self):
        return self.num_students_needed

    def get_num_students(self):
        return self.num_students

    def get_id(self):
        return self.id

def get_num_students_needed(rooms):
    num_students_needed = 0
    for room in rooms:
        num_students_needed += room.get_num_students_needed()
    return num_students_needed

def get_num_students(rooms):
    num_students = 0
    for room in rooms:
        num_students += room.get_num_students()
    return num_students

def dfs(rooms, visited, order):
    if len(visited) == len(rooms):
        if get_num_students_needed(rooms) == get_num_students(rooms):
            return order
        else:
            return None
    for i, room in enumerate(rooms):
        if i in visited:
            continue
        visited.add(i)
        order.append(room.get_id())
        for room in rooms:
            room.add_students_needed(room.get_num_students())
        for room in rooms:
            room.add_exam(room.get_num_students())
        if room.get_num_students_needed() > room.get_num_students():
            break
        for room in rooms:
            room.add_students_needed(-room.get_num_students())
            room.add_exam(-room.get_num_students())
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
