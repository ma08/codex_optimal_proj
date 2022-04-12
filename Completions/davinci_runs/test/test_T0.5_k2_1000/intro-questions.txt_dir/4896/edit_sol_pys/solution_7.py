
def main():
    n = int(input()) # number of people
    people = [int(x) for x in input().split()] # get people
    groups = [] # list of groups
    for person in people: # iterate through people
        if len(groups) == 0: # if no groups
            groups.append(person) # add first person
        else: # if there are groups
            if person > groups[-1]: # if person is bigger than last person in group
                groups.append(person) # add person to group
    print(len(groups)) # print number of groups

main()
