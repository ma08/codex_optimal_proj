

N = int(raw_input())

class Person:
    def __init__(self, id, testimonies):
        self.id = id
        self.testimonies = testimonies
        self.kind = None

def find_max_honest_persons():
    people = []
    for i in range(N):
        testimonies = []
        for j in range(int(raw_input())):
            testimony = [int(x) for x in raw_input().split(" ")]
            testimonies.append(testimony)
        people.append(Person(i + 1, testimonies))

    people = set_kind_of_people_recursively(people)

    max_honest_persons = 0
    for person in people:
        if person.kind == "h":
            max_honest_persons += 1
    return max_honest_persons

def set_kind_of_people_recursively(people):
    for person in people:
        if person.kind is None:
            set_kind_of_person(person, people)
    return people

def set_kind_of_person(person, people):
    if person.kind is None:
        person.kind = "h"
        for testimony_id, is_honest in person.testimonies:
            if is_honest == 1 and not people[testimony_id - 1].kind == "h":
                person.kind = "u"
                break
        for testimony_id, is_honest in person.testimonies:
            if is_honest == 0 and people[testimony_id - 1].kind == "h":
                people[testimony_id - 1].kind = "u"
                set_kind_of_people_recursively(people)
                break

print find_max_honest_persons()
