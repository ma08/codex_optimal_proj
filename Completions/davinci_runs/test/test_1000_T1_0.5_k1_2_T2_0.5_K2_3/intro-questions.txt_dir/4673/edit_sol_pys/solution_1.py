

def person_lister(func):
    def inner(people_list):
        # complete the function
        return list(map(func,sorted(people_list,key=lambda x: int(x[2]))))
    return inner

@person_lister
def name_format(person_list):
    return ("Mr. " if person_list[3] == "M" else "Ms. ") + person_list[0] + " " + person_list[1]

if __name__ == '__main__':
    people_list = [input().split() for i in range(int(input()))]
    print(*name_format(people_list), sep='\n')
